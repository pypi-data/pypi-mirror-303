import argparse

from xmanager import xm

import xm_slurm
from xm_slurm.console import console


async def logs(
    experiment_id: int,
    wid: int,
    *,
    follow: bool = True,
    num_lines: int = 10,
    block_size: int = 1024,
):
    wu = xm_slurm.get_experiment(experiment_id).work_units()[wid]
    async for log in wu.logs(num_lines=num_lines, block_size=block_size, wait=True, follow=follow):
        console.print(log, end="\n")


@xm.run_in_asyncio_loop
async def main():
    parser = argparse.ArgumentParser(description="XManager.")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    logs_parser = subparsers.add_parser("logs", help="Display logs for a specific experiment.")
    logs_parser.add_argument("xid", type=int, help="Experiment ID.")
    logs_parser.add_argument("wid", type=int, help="Work Unit ID.")
    logs_parser.add_argument(
        "-n",
        "--n-lines",
        type=int,
        default=50,
        help="Number of lines to display from the end of the log file.",
    )
    logs_parser.add_argument(
        "-f",
        "--follow",
        default=True,
        action="store_true",
        help="Follow the log file as it is updated.",
    )

    args = parser.parse_args()
    match args.subcommand:
        case "logs":
            await logs(args.xid, args.wid, follow=args.follow, num_lines=args.n_lines)


if __name__ == "__main__":
    main()  # type: ignore
