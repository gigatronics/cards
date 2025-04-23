class RiskScoreController {
    constructor(private riskScoreService: RiskScoreService) {}

    postRiskScore(req: Request, res: Response) {
        const { score } = req.body;
        const analysis = this.riskScoreService.analyzeRiskScore(score);
        res.json(analysis);
    }

    analyzeRiskScore(req: Request, res: Response) {
        const { score } = req.body;
        const result = this.riskScoreService.calculateScore(score);
        const reasons = this.riskScoreService.getReasons(score);
        res.json({ score: result, reasons });
    }
}

export default RiskScoreController;