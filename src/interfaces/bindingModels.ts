
// Job items
// jobType: is used to classify job based on their discpline/ degree relevance
// jobLoc: location of the job (where will the job be taking place)
// jobDesc: descript of the job
export interface JobItem {
    id: string;
    endDate: string;
    jobTitle: string;
    jobCompany: string;
    jobType: string;
    jobLoc: string;
    jobDes: string;
    jobUrl: string;
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