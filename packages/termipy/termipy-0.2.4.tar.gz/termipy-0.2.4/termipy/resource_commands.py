"""
Resource-related commands for TermiPy.

This module contains commands that deal with system resource usage.
"""

import psutil
import time
from typing import List
from termipy.base_command import Command
from colorama import Fore, Back, Style, init
import re

init(autoreset=True)

class ResourceUsageCommand(Command):
    def __init__(self):
        self.max_width = self.calculate_max_width()
        self.output = []

    def calculate_max_width(self) -> int:
        """Calculate the maximum width needed for all resource sections."""
        titles = [
            "CPU Usage",
            "Memory Usage",
            "Disk Usage",
            "Network Usage",
            "Process Usage"
        ]
        
        content_widths = [
            len(f"CPU Usage: 100%"),
            len(f"Memory Usage: 100%"),
            len(f"Disk Usage: 100%"),
            len(f"Network Bytes Sent: 100 MB"),
            len(f"PID: 9999, Name: ProcessName, CPU: 100%")
        ]
        
        return max(max(len(title) for title in titles), max(content_widths)) + 4

    def strip_ansi(self, text):
        """Remove ANSI escape codes from a string."""
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def print_in_block(self, title: str, content: List[str]):
        """Encloses the title and content inside a rectangular block."""
        block_width = self.max_width

        self.output.append(f"┌{'─' * block_width}┐")
        self.output.append(f"│ {Fore.CYAN}{title.ljust(block_width - 2)}{Style.RESET_ALL} │")
        self.output.append(f"├{'─' * block_width}┤")
        for line in content:
            stripped_line = self.strip_ansi(line)
            padding = block_width - len(stripped_line) - 2
            self.output.append(f"│ {line}{' ' * padding} │")
        self.output.append(f"└{'─' * block_width}┘")
        self.output.append("")

    def color_percentage(self, percentage: float) -> str:
        """Returns a colored string based on the percentage."""
        if percentage >= 90:
            return f"{Fore.RED}{percentage:.1f}%{Style.RESET_ALL}"
        elif percentage >= 70:
            return f"{Fore.YELLOW}{percentage:.1f}%{Style.RESET_ALL}"
        else:
            return f"{Fore.GREEN}{percentage:.1f}%{Style.RESET_ALL}"

    def cpu_usage(self):
        """Displays CPU usage."""
        cpu_percent = psutil.cpu_percent(interval=1)
        title = "CPU Usage"
        content = [
            f"CPU Usage: {self.color_percentage(cpu_percent)}"
        ]
        self.print_in_block(title, content)

    def memory_usage(self):
        """Displays memory usage."""
        memory = psutil.virtual_memory()
        title = "Memory Usage"
        content = [
            f"Memory Usage: {self.color_percentage(memory.percent)}",
            f"Total Memory: {memory.total / (1024 ** 3):.2f} GB",
            f"Available Memory: {Fore.CYAN}{memory.available / (1024 ** 3):.2f} GB{Style.RESET_ALL}"
        ]
        self.print_in_block(title, content)

    def disk_usage(self):
        """Displays disk usage."""
        disk = psutil.disk_usage('/')
        title = "Disk Usage"
        content = [
            f"Disk Usage: {self.color_percentage(disk.percent)}",
            f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB",
            f"Free Disk Space: {Fore.CYAN}{disk.free / (1024 ** 3):.2f} GB{Style.RESET_ALL}"
        ]
        self.print_in_block(title, content)

    def network_usage(self):
        """Displays network usage."""
        net_io = psutil.net_io_counters()
        title = "Network Usage"
        content = [
            f"Network Bytes Sent: {Fore.YELLOW}{net_io.bytes_sent / (1024 ** 2):.2f} MB{Style.RESET_ALL}",
            f"Network Bytes Received: {Fore.YELLOW}{net_io.bytes_recv / (1024 ** 2):.2f} MB{Style.RESET_ALL}"
        ]
        self.print_in_block(title, content)

    def process_usage(self):
        """Displays top 5 CPU-consuming processes."""
        processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                           key=lambda x: x.info['cpu_percent'], reverse=True)[:5]
        title = "Process Usage (Top-5)"
        content = [f"PID: {Fore.CYAN}{proc.info['pid']}{Style.RESET_ALL}, "
                   f"Name: {Fore.YELLOW}{proc.info['name']}{Style.RESET_ALL}, "
                   f"CPU: {self.color_percentage(proc.info['cpu_percent'])}"
                   for proc in processes]
        self.print_in_block(title, content)

    def execute(self, args: List[str]) -> bool:
        """Continuously monitor and display resource usage until interrupted."""
        try:
            while True:
                self.output = []
                self.cpu_usage()
                self.memory_usage()
                self.disk_usage()
                self.network_usage()
                self.process_usage()
                self.output.append(f"{Fore.YELLOW}Press Ctrl+C to STOP monitoring.{Style.RESET_ALL}")

                # Clear the screen and move cursor to top-left
                print("\033[2J\033[H", end="")
                
                # Print the entire output at once
                print("\n".join(self.output))

                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}Stopped monitoring resource usage.{Style.RESET_ALL}")
        
        return True