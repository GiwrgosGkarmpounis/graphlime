from graphlime import GraphLIME

number_of_node = 0 # the specific node to be explained

explainer = GraphLIME(model, hop=2, rho=0.1, cached=True)
coefs = explainer.explain_node(number_of_node, features, edge_index_houses)
print(coefs) 
print(coefs.shape)

# Visualize the coefficients (β values)
plt.figure(figsize=(16, 4))

x = list(range(data.num_node_features))

plt.bar(x, coefs, width=1.0)
plt.xlabel('Feature Index')
plt.ylabel(r'$\beta$');

plt.show()

print(f'The {np.argmax(coefs)}-th feature is the most important.')

# find also all the other important features
# value in enumerate(test_list) if value == 3
res_list = [i for i, value in enumerate(coefs) if value != 0]
print("All the features influencing this node are ", res_list)

# We can also write code to find the top 3 features for example or top 5!!
#sorted_list = sorted(res_list)
#print(sorted_list)

list_of_features = []
list_of_names = []
my_dict = {'NumberOfRooms': [], 'Size': [], 'ConstructionDate': [], 'NumberOfLevels': [], 'NumberOfBathrooms': [],
           'NumberOfWc': [], 'Latitude': [], 'Longitude': [], 'TypeId': [], 'SubTypeId': [], 'ActionId': [],
           'HeatingTypeId': [], 'BasicHeatingTypeId': [], 'FloorLevelId': [], 'DistanceFromCoast': []}
for i, value in enumerate(coefs):
  if value != 0:
    print("feature:", names[i] , "with value:", value)
    list_of_features.append(value)
    list_of_names.append(names[i])
    my_dict[names[i]].append(value)
print("list of features (values):", sorted(list_of_features, reverse=True))
print("list of names:", list_of_names)
print(my_dict)
sorted_dict = sorted(my_dict.items(), lambda x:x[1])
print(sorted_dict)
