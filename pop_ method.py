#pop method
#removing an item from a list but keeping the item

subscribers = ['esben@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

poppped_subscriber = subscribers.pop()
print(subscribers)
print(poppped_subscriber)

subscribers = ['esben@example.com', 'john@example.com', 'mary@example.com']
first_subscriber = subscribers.pop(0)

print("Your first subscriber was " + first_subscriber + ".")

subscribers = ['esben@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

subscribers.remove('esben@example.com')
print(subscribers)

subscribers = ['esben@example.com', 'john@example.com', 'mary@example.com']
subscribed_by_mistake = "john@example.com"
subscribers.remove(subscribed_by_mistake)
print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")

