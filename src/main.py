import os
import sys
import random as rand
from colorama import Fore
import time

source_url = "github.com/exterpolation/VRAP"
author = "Lexia"
author_discord = "tickflow"

agent_pool = ["Astra", "Brimstone", "Clove", "Harbor", "Omen", "Viper", "Chamber", "Cypher",
              "Deadlock", "Killjoy", "Sage", "Breach", "Fade", "Gekko", "KAY/O", "Skye", "Sova", "Iso", "Jett", "Neon",
              "Phoenix", "Raze", "Reyna", "Yoru"]


def animated_dots(duration=5, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        for dots in range(4):
            yield '.' * dots + ' ' * (3 - dots)
            time.sleep(interval)


def greet_user() -> str:
    return f"Welcome to VRAP (Valorant Agent Random Picker), {os.getlogin()}!"


def print_agent_pool():
    print(f"\n    {Fore.GREEN}[!] Current agent pool:")
    for i, agent in enumerate(agent_pool, 1):
        print(f"    {Fore.CYAN}{i}. {agent}")


def modify_agent_pool():
    print_agent_pool()
    while True:
        action = input(f"\n    {Fore.YELLOW}[?] Add or remove agents? (a/r): ").lower().strip()
        if action in ['a', 'r']:
            break
        else:
            print(f"    {Fore.RED}[!] Invalid action. Please enter 'a' to add or 'r' to remove agents.")

    agents = input(f"\n    {Fore.YELLOW}[?] Enter agents (comma-separated): ").strip().split(",")
    agents = [agent.strip().title() for agent in agents]

    if action == "a":
        for agent in agents:
            if agent not in agent_pool:
                agent_pool.append(agent)
            else:
                print(f"{Fore.RED}[!] {agent} is already in the pool.")
    elif action == "r":
        for agent in agents:
            if agent in agent_pool:
                agent_pool.remove(agent)
            else:
                print(f"{Fore.RED}[!] {agent} is not in the pool.")
    print_agent_pool()


def main() -> int:
    print(fr"""{Fore.WHITE}
      ___      ___ ________  ________  ________
     |\  \    /  /|\   __  \|\   __  \|\   __  \
     \ \  \  /  / | \  \|\  \ \  \|\  \ \  \|\  \
      \ \  \/  / / \ \   _  _\ \   __  \ \   ____\
       \ \    / /   \ \  \\  \\ \  \ \  \ \  \___|
        \ \__/ /     \ \__\\ _\\ \__\ \__\ \__\
         \|__|/       \|__|\|__|\|__|\|__|\|__|

         [>]Source: {source_url}
         [>]Author: {author}
         [>]Discord: {author_discord}
    """)

    print(f"\n    {Fore.GREEN}[!] {greet_user()}")

    if input(f"\n    {Fore.YELLOW}[?] Modify agent pool? (y/N): ").lower().strip() == "n":
        print(f"\n    {Fore.GREEN}[!] Choosing a random agent", end='', flush=True)
        for dots in animated_dots(duration=5, interval=0.5):
            print(f'\r    {Fore.GREEN}[!] Choosing a random agent{dots}', end='', flush=True)
        print(f"\n    {Fore.GREEN}[!] Selected agent: {rand.choice(agent_pool)}")
        return 0

    while True:
        modify_agent_pool()
        if input(f"\n    {Fore.YELLOW}[?] Done modifying and select a random agent? (y/n): ").lower().strip() == "y":
            print(f"\n    {Fore.GREEN}[!] Choosing a random agent", end='', flush=True)
            for dots in animated_dots(duration=5, interval=0.5):
                print(f'\r    {Fore.GREEN}[!] Choosing a random agent{dots}', end='', flush=True)
            print(f"\n    {Fore.GREEN}[!] Selected agent: {rand.choice(agent_pool)}")
            break

    return 0


if __name__ == '__main__':
    sys.exit(main())
