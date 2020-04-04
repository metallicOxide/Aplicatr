export interface JobItem {
    title: string;
    link: string;
    summary: string;
    closing_Date: string;
    location: string;
}

export interface CalendarItemBindingModel {
    title: string;
    link: string;
    summary: string;
    chosen_Date: string;
    location: string;
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