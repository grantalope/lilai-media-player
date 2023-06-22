# Use the official Node.js 16 image.
FROM node:16

# Set the working directory.
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install production dependencies.
RUN npm install

# Copy the local code to the container's workspace.
COPY . ./

# Build the application
RUN npm run build

# Start the application
CMD [ "npm", "start" ]
