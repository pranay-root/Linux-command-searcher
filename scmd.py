import sys

commands = {
    "search port": "sudo ss -tulpn",
    "install package": "sudo apt install <package_name>",  # Adjust for other distros
    "start apache server": "sudo systemctl start apache2",
    "stop apache server": "sudo systemctl stop apache2",
    "restart apache server": "sudo systemctl restart apache2",
    "list running process": "sudo ps aux",
    "real time process": "sudo top",
    "active listening ports": "sudo netstat -tulpn",
    "search tool": "sudo grep <keyword>"
    # Add more commands as needed
}

def find_matching_command(search_terms):
  """Finds a command that matches any of the search terms.

  Args:
    search_terms: A list of search terms.

  Returns:
    The matching command or None if no match is found.
  """
  for command, command_terms in commands.items():
    if any(term in command_terms for term in search_terms):
      return command
  return None

def main():
  search_terms = " ".join(sys.argv[1:]).lower().split()  

  matching_command = find_matching_command(search_terms)

  if matching_command:
    print(commands[matching_command])
  else:
    print("No matching command found.")

if __name__ == "__main__":
  main()
