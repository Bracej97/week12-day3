# Back-end Mocking

## Challenge

When collaborating on group projects, developing the frontend of an application can be challenging when the backend is still under development. In this exercise, you will explore and experiment with a technique to build out data and functionality that mocks the backend of a website. This allows frontend development to proceed independently without being blocked by incomplete backend functionality.

Review the code in `data/api.jsx` and the `mocks` folder to understand how mocking works and how it can enable seamless progress in group projects.

## Key Learnings

- Understanding the concept and importance of back-end mocking in collaborative development.
- How to use mock data and functionality to simulate API responses.
- The role of mocking in reducing interdependence and ensuring smooth development workflows.

## User Story

- As a developer, I want to mock back-end functionality, so I can develop and test the frontend independently while waiting for the backend to be built.

## Acceptance Criteria

1. **Understand the existing mock setup**:

   - Open and review the `data/api.jsx` file to understand how API calls are being mocked.
   - Explore the `mocks` folder to examine the data structure and see how the mock data is organized.

2. **Implement and test a mocked API call**:

   - Use the existing mock API framework to add a new mocked API endpoint.
   - Test the endpoint by making a call from the frontend to ensure it returns the correct mocked data.

3. **Simulate error responses**:

   - Modify the mock setup to simulate an error response for one of the endpoints (e.g., a `404 Not Found` or `500 Internal Server Error`).
   - Handle the error gracefully in the frontend and display an appropriate message to the user.

4. **Verify front-end functionality with mock data**:
   - Ensure that the frontend application can use the mock data to display relevant UI elements.
   - Confirm that no real backend dependency is required for the functionality to work.

## Bonus Challenge

- Explore a library like `msw` (Mock Service Worker) to mock API requests at the network level for enhanced flexibility.
- Use mock data to test edge cases, such as large datasets or unexpected API responses, to improve the robustness of your frontend application.

Happy mocking!
