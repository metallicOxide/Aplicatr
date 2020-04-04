
// get the api route for the environment
// dynamically change during production build
// the value for production and development can be changed 
// in the .env file
const ApiBase = process.env.VUE_APP_API_URL;

export const ApiRoutes = {
    loginRoute: `${ApiBase}/jobs/login`,
    calendarRoute: `${ApiBase}/jobs/calendar`,
    jobsRoute: `${ApiBase}/jobs`
}