#!/usr/bin/env python
import os
import shutil
from argparse import ArgumentParser, REMAINDER
from .utils import configs, modify_config_file, get_free_gpus, get_python_cmd, remove_compiled_prefix, generate_hps, show_strategies

def main():
    parser = ArgumentParser(description="AcceleratorModule CLI to run train processes on top of 🤗 Accelerate.")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Run distributed training
    launch_parser = subparsers.add_parser("launch", help="Launch distributed training processes.")
    launch_parser.add_argument(
        "--gpus",
        "-n",
        default="all",
        type=str,
        required=False,
        help="Number or GPU indices to use (e.g. -n=0,1,4,5 | -n=all | -n=available)."
    )
    launch_parser.add_argument(
        "-N",
        default="0",
        type=str,
        required=False,
        help="Number of GPUs to use. This does not consider GPU indices by default, although you can represent "
             "a Python slice. (e.g. '2:', which means from index 2 to the last GPU index, or "
             "'3:8', which means from index 3 to index 7, or lastly ':4', which means indices 0 to 3 or a total of 4 gpus)."
    )
    launch_parser.add_argument(
        "--strat",
        type=str,
        required=False,
        default="ddp",
        help="Parallelism strategy to apply or config file path. See 'accmt strats'."
    )
    launch_parser.add_argument("-O1", action="store_true", help="Apply optimization type 1: efficient OMP_NUM_THREADS.")
    launch_parser.add_argument("file", type=str, help="File to run training.")
    launch_parser.add_argument("extra_args", nargs=REMAINDER)
    
    # Get model from checkpoint
    get_parser = subparsers.add_parser("get", help="Get model from a checkpoint directory.")
    get_parser.add_argument("checkpoint", type=str, help="Checkpoint directory.")
    get_parser.add_argument("--out", "-O", "-o", required=True, type=str, help="Output directory path name.")
    get_parser.add_argument("--dtype", type=str, default="float32", help=(
        "Data type of model parameters. Available options are all "
        "those from PyTorch ('float32', 'float16', etc)."
    ))

    # Strats
    strats_parser = subparsers.add_parser("strats", help="Available strategies.")
    strats_parser.add_argument("--ddp", action="store_true", help="Only show DistributedDataParallel (DDP) strategies.")
    strats_parser.add_argument("--fsdp", action="store_true", help="Only show FullyShardedDataParallel (FSDP) strategies.")
    strats_parser.add_argument("--deepspeed", action="store_true", help="Only show DeepSpeed strategies.")

    # Generate example
    example_parser = subparsers.add_parser("example", help="Generate example file.")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        exit(0)

    import torch

    if args.command == "launch":
        gpus = args.gpus.lower()
        strat = args.strat
        file = args.file
        extra_args = " ".join(args.extra_args)

        if "." in strat:
            accelerate_config_file = strat
        else:
            accelerate_config_file = configs[strat]

        if not torch.cuda.is_available():
            raise ImportError("Could not run CLI: CUDA is not available on your PyTorch installation.")

        NUM_DEVICES = torch.cuda.device_count()

        gpu_indices = ""
        if gpus == "available":
            gpu_indices = ",".join(get_free_gpus(NUM_DEVICES))
        elif gpus == "all":
            gpu_indices = ",".join(str(i) for i in range(NUM_DEVICES))
        else:
            gpu_indices = gpus.removeprefix(",").removesuffix(",")

        if gpu_indices == "":
            raise RuntimeError("Could not get GPU indices. If you're using 'available' in 'gpus' "
                            "parameter, make sure there is at least one GPU free of memory.")

        if args.N != "0":
            if ":" in args.N:
                _slice = slice(*map(lambda x: int(x.strip()) if x.strip() else None, args.N.split(':')))
                gpu_indices = ",".join([str(i) for i in range(NUM_DEVICES)][_slice])
            else:
                gpu_indices = ",".join(str(i) for i in range(int(args.N)))

        num_processes = len(gpu_indices.split(","))
        modify_config_file(accelerate_config_file, num_processes)
        
        optimization1 = f"OMP_NUM_THREADS={os.cpu_count() // num_processes}" if args.O1 else ""

        cmd = (f"{optimization1} CUDA_VISIBLE_DEVICES={gpu_indices} "
                f"accelerate launch --config_file={accelerate_config_file} "
                f"{file} {extra_args}")
        
        os.system(cmd)
    elif args.command == "get":
        assert args.out is not None, "You must specify an output directory ('--out')."
        assert hasattr(torch, args.dtype), f"'{args.dtype}' not supported in PyTorch."
        CHKPT_BASE_DIRECTORY = f"{args.checkpoint}/checkpoint"
        checkpoint_dir = CHKPT_BASE_DIRECTORY if os.path.exists(CHKPT_BASE_DIRECTORY) else args.get
        files = os.listdir(checkpoint_dir)

        python_cmd = get_python_cmd()
        os.makedirs(args.out, exist_ok=True)
        if "status.json" in os.listdir(args.checkpoint):
            shutil.copy(f"{args.checkpoint}/status.json", args.out)
        
        state_dict_file = f"{args.out}/pytorch_model.pt"

        if "zero_to_fp32.py" in files: # check for DeepSpeed
            print("Converting Zero to float32 parameters...")
            exit_code = os.system(f"{python_cmd} {checkpoint_dir}/zero_to_fp32.py {checkpoint_dir} {state_dict_file}")
            if exit_code != 0:
                raise RuntimeError("Something went wrong when converting Zero to float32.")
        elif "pytorch_model_fsdp_0" in files: # check for FSDP
            # using Accelerate's approach for now, and only checking for one node
            exit_code = os.system(f"accelerate merge-weights {checkpoint_dir}/pytorch_model_fsdp_0 {args.out}")
            if exit_code != 0:
                raise RuntimeError("Something went wrong when merging weights from FSDP.")
            
            shutil.copy(f"{checkpoint_dir}/pytorch_model.bin", f"{args.out}/pytorch_model.pt")
        else: # check for DDP
            shutil.copy(f"{checkpoint_dir}/pytorch_model.bin", f"{args.out}/pytorch_model.pt")
            
        state_dict = torch.load(state_dict_file, map_location="cpu", weights_only=True)
        state_dict = remove_compiled_prefix(state_dict)

        _dtype_str = f" and converting to dtype {args.dtype}" if args.dtype is not None else ""
        print(f"Setting 'requires_grad' to False{_dtype_str}...")
        for key in state_dict.keys():
            state_dict[key].requires_grad = False
            if args.dtype is not None:
                state_dict[key] = state_dict[key].to(getattr(torch, args.dtype))

        torch.save(state_dict, state_dict_file)
        print(f"Model directory saved to '{args.out}'.")
    elif args.command == "strats":
        if args.ddp:
            show_strategies(filter="ddp")
        elif args.fsdp:
            show_strategies(filter="fsdp")
        elif args.deepspeed:
            show_strategies(filter="deepspeed")
        else:
            show_strategies()
    elif args.command == "example":
        generate_hps()
        print("'hps_example.yaml' generated.")

if __name__ == "__main__":
    main()
