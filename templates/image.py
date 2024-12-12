import graphviz

# Create a new directed graph
dot = graphviz.Digraph(comment='ClearSky Project Architecture')

# Adding AWS components
dot.node('A', 'AWS API Gateway')
dot.node('B', 'AWS Lambda')
dot.node('C', 'AWS DynamoDB')
dot.node('D', 'AWS CloudWatch')
dot.node('E', 'AWS SNS')

# Defining the relationships between components
dot.edge('A', 'B', label='API Calls')
dot.edge('B', 'C', label='Read/Write Data')
dot.edge('B', 'D', label='Logging')
dot.edge('B', 'E', label='Notifications')

# Optionally add some more edges to represent user interactions
dot.node('F', 'User Dashboard', shape='rect')
dot.edge('F', 'A', label='API Requests')

# Visualize the diagram
dot.render('ClearSky_Architecture', format='png', cleanup=True)

print("Project Diagram Generated: ClearSky_Architecture.png")