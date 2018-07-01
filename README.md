# RestfullHappyApp
Demonstrate restfull application running in container


1. Building Happiness App:

  docker build -t happyapp .

2. Running the image:
       docker run -it -d -p 5000:80  happyapp

3. Testing via Browser:
      http://localhost:5000/happiness/events/2
