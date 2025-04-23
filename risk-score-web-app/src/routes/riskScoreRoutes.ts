import { Router } from 'express';
import { RiskScoreController } from '../api/riskScoreController';

const router = Router();
const riskScoreController = new RiskScoreController();

export function setRiskScoreRoutes(app: Router) {
    app.post('/api/risk-score', riskScoreController.postRiskScore.bind(riskScoreController));
    app.get('/api/risk-score/analyze', riskScoreController.analyzeRiskScore.bind(riskScoreController));
}