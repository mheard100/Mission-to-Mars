#To get started with Mongo, first open a new terminal window, but make sure your working environment is activated. Note that your environment does not need to have the same name as the one in the image.
#Then, to start an instance, type mongod into the first line of your terminal and press return or enter on your keyboard
#In our terminal, create a second window or tab to use for working in Mongo. Again, make sure your environment is active.

#On the first line of this new window, type "mongo." This is done in a new window because, after you execute the command, you cannot use the terminal for other tasks—only to send information to and from the database.
#In the terminal where Mongo is active and awaiting instruction, type "use practicedb" and then press Enter. This creates a new database named "practicedb" and makes it our active database.
#If you're not sure which database you're using, type "db" in the terminal and press Enter.
#After typing "db" into the terminal and pressing Enter, the name of the current active database is returned. This is a quick check to make sure we'll be saving data to the right spot.

#Now that we've confirmed we're in the right database, we can practice the commands to insert data or a document.
#The syntax follows: db.collectionName.insertOne({key:value}). 
#example: db.zoo.insertOne({name: 'Cleo', species: 'jaguar', age: 12, hobbies: ['sleeping', 'eating', 'climbing']})

#Now that we've added data to our collection, when we type "show collections" we'll actually see a result: zoo. 
#Executing db.zoo.find() in the terminal will return each of the documents we've already added.

#Documents can also be deleted or dropped. The syntax to do so follows: db.collectionName.deleteOne({})

#So, if we wanted to remove Cleo from the database, we would update that line of code to:

#db.zoo.deleteOne({name: 'Cleo'})

#We can also empty the collection at once, instead of one document at a time. For example, to empty our pets collection, we would type: db.zoo.remove({}). Because the inner curly brackets are empty, Mongo will assume that we want everything in our pets collection to be removed.

#Additionally, to remove a collection all together, we would use db.zoo.drop(). After running that line in the shell, our pets collection will no longer exist at all.

#And to remove the test database, we will use this line of code: db.dropDatabase()

#You can quit the Mongo shell by using keyboard commands: Command + C for Mac or CTRL + C for Windows. This stops the processes that are actively running and frees up your terminal. Remember to quit both the server and the shell when you're done practicing. Otherwise, they'll continue to run in the background and use system resources, such as memory, and slow down the response time of your computer.


