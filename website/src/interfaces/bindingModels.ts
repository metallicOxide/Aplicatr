export interface JobItem {
    title: string;
    link: string;
    summary: string;
    closing_date: string;
    location: string;
}

export interface CalendarItemBindingModel {
    title: string;
    link: string;
    summary: string;
    chosen_date: string;
    location: string;
}

export interface CalendarBindingModel {
    jobs: Array<CalendarItemBindingModel>;
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