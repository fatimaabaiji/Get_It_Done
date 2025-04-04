# GET It Done

## Project Overview
Get It Done is a Full-Stack Django web application designed to help users manage their tasks efficiently. The project follows Agile methodology and includes core features like task creation, editing, deletion, completion, reminders, and prioritization.

## Prioritization System (MoSCoW)
Note: Initially planned to implement the MoSCoW prioritization system, but due to time constraints, this was postponed. It remains on the to-do list for future enhancements.

## User Stories
- As a user, I want to create tasks to manage my to-do list.
- As a user, I want to edit tasks to update my to-do list.
- As a user, I want to delete tasks to remove completed or irrelevant items.
- As a user, I want to prioritize tasks to focus on important items first.

## Features
- Task creation, editing, deletion, and prioritization.
- User authentication and role-based access control.
- Real-time notifications using Django Channels.
- Responsive design for different devices.

## Design and User Experience
- Simple wireframe for easy navigation.
- Bootstrap for front-end styling.
- User-friendly design for task management.

Note: Initially, I considered adding a search feature for tasks, but time constraints prevented its implementation. Additionally, I kept iterating on the design and layout as I was not fully satisfied with the results.

### Wireframes
![Alt text](static/images/IMG_2139.jpeg)
![Alt text](static/images/IMG_2140.jpeg)
![Alt text](static/images/IMG_2141.jpeg)

### Screenshots
![Alt text](static/images/IMG_2138.jpeg)

## Agile Methodology
- Project managed using Agile principles.
- Tasks tracked on the GitHub Project Board.

## Testing
- Unit tests implemented for views, models, and forms using Django’s testing framework.
- Simple design tests for front-end elements.
- Automated testing procedures documented.

### Test Results
 Performance
Achieved a performance score of 90+ using Lighthouse testing.

Optimized images, minimized CSS and JavaScript, and used efficient rendering for faster load times.

##best pactices
Maintained a best practices score of 90+.

Followed clean code principles, reduced console errors, and ensured accessibility compliance.

##Testing Tools Used
Lighthouse for performance and best practice evaluation.

Manual Testing across different browsers and devices to ensure responsiveness.

## Deployment
- Deployed on Heroku.
- Follow the README guide for setting up the environment and configuring dependencies.

## Challenges Faced
- Initially struggled with the design and encountered issues while accessing the app. It appeared to load slowly, possibly due to internet issues or server configurations.
- Only one model was used in the tasks app. Ideally, an additional model for accounts should have been created, but due to time constraints, I decided to proceed without it.
- The favicon didn't work as intended despite attempts to fix it.
- The wireframe and design remained simple due to limited time.

## Future Improvements
- Add an accounts model for better structure.
- Implement better error handling.
- Optimize performance and ensure smoother loading.
- Improve overall UI/UX with a more modern design.
- Implement the MoSCoW prioritization system.
- Add a task search feature.

## Future Improvements

- Improve the UI design to ensure form elements like **Due Date** and **Priority Selection** fit their containers properly across all screen sizes.
- Troubleshoot CSS issues to ensure consistent styling across all components.
- Continue refining the user experience for better accessibility and usability.

## Credits
- Bootstrap for front-end design.
- Django for the web framework.
- PostgreSQL for the database.

## Final Thoughts
Although there were challenges, the project successfully implements core features. With more time, additional improvements could be made to enhance the user experience. This project also provided valuable insights into full-stack development using Django and Heroku.