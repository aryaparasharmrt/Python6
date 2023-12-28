import subprocess

print('Running repository management tasks...')

# Example: Print the list of branches
branches = subprocess.check_output(['git', 'branch']).decode('utf-8')
print('Branches:', branches)
