import subprocess
import click
from rich.console import Console
from rich.table import Table
from collections import defaultdict

def get_network_processes():
    try:
        output = subprocess.check_output(["lsof", "-i", "-P", "-n"], text=True)
        lines = output.split('\n')
        processes = defaultdict(set)
        for line in lines[1:]:  # Skip the header line
            if line:
                parts = line.split()
                if len(parts) >= 9:
                    pid = parts[1]
                    name = parts[0]
                    port = parts[8].split(':')[-1]
                    processes[(pid, name)].add(port)
        return processes
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve network processes. Make sure you have the necessary permissions.")
        return defaultdict(set)

@click.command()
@click.option('--all', is_flag=True, help="See all processes.")
@click.option('-i', '--include-ports', help="Comma-separated list of ports to include.")
@click.option('-x', '--exclude-ports', help="Comma-separated list of ports to exclude.")
@click.option('--page', is_flag=True, help="Page the output.")
def cli(all, include_ports, exclude_ports, page):
    processes = get_network_processes()
    
    if include_ports:
        include_ports = set(p.strip() for p in include_ports.split(','))
        processes = {k: v.intersection(include_ports) for k, v in processes.items() if v.intersection(include_ports)}
    
    if exclude_ports:
        exclude_ports = set(p.strip() for p in exclude_ports.split(','))
        processes = {k: v.difference(exclude_ports) for k, v in processes.items()}
        processes = {k: v for k, v in processes.items() if v}
    
    table = Table(title="Network Processes")
    table.add_column("PID", style="cyan")
    table.add_column("Process Name", style="magenta")
    table.add_column("Ports", style="green")
    
    sorted_processes = sorted(processes.items(), key=lambda x: (min(int(p) if p != '*' else float('inf') for p in x[1]), x[0]))
    
    if not all:
        sorted_processes = sorted_processes[:10]  # Show only first 10 processes if --all is not specified
    
    for (pid, name), ports in sorted_processes:
        ports_str = ', '.join(sorted(ports, key=lambda x: int(x) if x != '*' else float('inf')))
        table.add_row(pid, name, ports_str)
    
    console = Console()
    if page:
        with console.pager():
            console.print(table)
            console.print(f"\nTotal processes displayed: {len(sorted_processes)}")
    else:
        console.print(table)
        console.print(f"\nTotal processes displayed: {len(sorted_processes)}")

if __name__ == "__main__":
    cli()
