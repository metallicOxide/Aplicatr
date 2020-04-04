export interface JobItem {
    title: string;
    link: string;
    summary: string;
    closingDate: string;
    location: string;
}

export interface CalendarItemBindingModel {
    title: string;
    link: string;
    summary: string;
    chosenDate: string;
    location: string;
}

export interface Credentials {
    Username: string;
    Password: string;
    Uni: string;
}

export interface LoginBindingModel {
    Username: string;
    Password: string;
    Uni: string;
}

export interface SearchBindingModel {
    Keywords: string;
    Location: string;
}

// List of job items
export interface JobItemList {
    jobList: JobItem[];
}

// model for generating ics file
export interface CalendarItem {
    startDateTime: string;
    endDateTime: string;
    jobTitle: string;
    jobLoc: string;
    jobDes: string;
    jobUrl: string;
}

// calendar list
export interface CalendarList {
    calendarList: CalendarItem[];
}