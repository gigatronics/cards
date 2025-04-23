export interface RiskScoreRequest {
    score: number;
}

export interface RiskScoreResponse {
    score: number;
    reasons: string[];
}