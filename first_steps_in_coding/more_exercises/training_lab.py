length = float(input())
width = float(input())

workspace_in_length = (length * 100) // 120
workspace_in_width = ((width * 100) - 100) // 70

total_workspaces = (workspace_in_width * workspace_in_length) - 3

print(int(total_workspaces))
