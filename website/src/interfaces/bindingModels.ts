export interface JobItem {
    title: string;
    company: string;
    link: string;
    summary: string;
    closing_date: string;
    location: string;
}

export interface CalendarBindingModel {
    jobs: Array<JobItem>;
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