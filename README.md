# Chess Website Project Report

## How to Run the Project

Clone the repositiory using '''git clone https://github.com/Shreyas529/chess-website.'''
Then change your directory to the chess-website directory in your terminal and run the command '''pip install -r requirments.txt'''.
Open and run server.py in your choice of code editor or run python server.py in your terminal

## Overview

The Chess Website project is a comprehensive web application aimed at providing chess enthusiasts with a platform to access various chess-related information and features. The project encompasses functionalities such as user authentication, displaying chess news, leaderboards, tournament details, chess rules, opening strategies, and user profile statistics. Additionally, users can log in using their Lichess accounts, making it easier to manage their chess-related activities.

## Objectives

The main objectives of the Chess Website project are:

1. **User Authentication:** Implement a secure user authentication system that allows users to sign up, log in, and log out. Users can also log in using their Lichess accounts, enhancing convenience.

2. **Chess News:** Display the latest chess news from a reliable source. Users who are logged in can access the news articles and stay updated with the chess community.

3. **Leaderboards:** Present the top players' leaderboard to showcase the most skilled chess players. The leaderboard reflects real-time rankings and achievements.

4. **Tournament Details:** Provide information about FIDE tournaments of the year, including dates, locations, and participants. Users can explore upcoming tournaments and plan their participation accordingly.

5. **Chess Rules:** Offer a comprehensive guide to chess rules for both beginners and advanced players. Users can access this resource to improve their understanding of the game's rules and mechanics.

6. **Opening Strategies:** Present various chess opening strategies and tactics, assisting players in enhancing their gameplay techniques.

7. **User Profile Statistics:** For users who log in using their Lichess accounts, display their Lichess profile statistics, such as rating history, wins, losses, and more.

## Implementation Details

The project is implemented using the Flask web framework for the backend and HTML, CSS, and JavaScript for the frontend. It leverages SQLAlchemy for database management, allowing user data and other information to be stored securely. Web scraping techniques are used to extract chess-related content, such as news articles, player rankings, and tournament details.

The OAuth protocol is integrated to enable users to log in using their Lichess accounts securely. The project also incorporates email functionality to send password reset emails to users who forget their passwords.

## Challenges Faced

During the development of the Chess Website project, several challenges were encountered, including:

1. **Web Scraping Complexity:** Implementing web scraping to fetch real-time data from external sources required dealing with dynamic web content and handling changes in website structures.

2. **OAuth Integration:** Integrating OAuth for Lichess authentication required thorough understanding and proper configuration to ensure secure and reliable user logins.

3. **Design and UI:** Designing an intuitive and user-friendly UI while maintaining a consistent and visually appealing interface presented design challenges.

## Future Scope

The Chess Website project has significant potential for future enhancements, including:

1. **User-Generated Content:** Allowing users to contribute articles, game analysis, and tutorials to create a collaborative chess community.

2. **Interactive Chess Board:** Introducing an interactive chess board that enables users to play against AI or other users online.

3. **Enhanced User Profiles:** Expanding user profiles to include detailed game statistics, win-loss records, and tournament history.

4. **Real-Time Game Viewing:** Implementing a feature to watch ongoing chess games in real-time, with commentary and analysis.

5. **Chess Puzzles and Challenges:** Incorporating chess puzzles and challenges to help users improve their tactical and strategic skills.

## Conclusion

The Chess Website project is a comprehensive platform catering to chess enthusiasts by providing valuable resources, features, and interactive elements. Through user authentication, web scraping, and integration with Lichess, the project successfully delivers a user-friendly and engaging experience for chess players of all levels.
