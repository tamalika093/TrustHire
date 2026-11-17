
def analyze_job_offer(offer_text: str):
    """
    Analyse a job offer and identify suspicious warning signs.
    """

    suspicious_keywords = [
        "pay registration fee",
        "pay a registration fee",
        "registration fee required",
        "pay security deposit",
        "guaranteed job",
        "no interview required",
        "limited time offer",
        "pay training fee",
        "instant selection",
        "processing fee",
        "application fee",
        "upfront payment",
        "pay to get the job",
        "personal bank account",
        "share your otp",
        "send your password",
        "whatsapp only",
        "no experience required",
        "earn money instantly",
        "100% guaranteed placement",
        "confidential job offer",
        "urgent payment required"
    ]

    warning_explanations = {
        "pay registration fee": "The recruiter is asking the candidate to pay a registration fee.",
        "pay a registration fee": "The recruiter is asking the candidate to pay a registration fee.",
        "registration fee required": "The candidate is being asked to pay a registration fee before proceeding.",
        "pay security deposit": "The recruiter is requesting money before employment.",
        "guaranteed job": "A guaranteed job promise may be misleading.",
        "no interview required": "Skipping the normal interview process may be suspicious.",
        "limited time offer": "Urgent deadlines may pressure candidates into rushed decisions.",
        "pay training fee": "The candidate is being asked to pay for training.",
        "instant selection": "Instant selection without proper evaluation may be suspicious.",
        "processing fee": "The recruiter is requesting a processing payment.",
        "application fee": "The candidate is being asked to pay to apply.",
        "upfront payment": "The recruiter is requesting money in advance.",
        "pay to get the job": "The candidate is being asked to pay to secure employment.",
        "personal bank account": "A request involving a personal bank account needs careful verification.",
        "share your otp": "Sharing an OTP can expose the candidate's account to unauthorised access.",
        "send your password": "A legitimate recruiter should not need the candidate's password.",
        "whatsapp only": "Communication through WhatsApp only may make recruiter verification difficult.",
        "no experience required": "An unusually broad experience requirement may need further verification.",
        "earn money instantly": "Promises of instant earnings may be misleading.",
        "100% guaranteed placement": "Guaranteed placement claims should be independently verified.",
        "confidential job offer": "A confidential offer may make independent verification difficult.",
        "urgent payment required": "Pressure to make an urgent payment is a warning sign."
    }

    detected_warnings = []
    offer = offer_text.lower()

    for keyword in suspicious_keywords:
        if keyword in offer:
            detected_warnings.append(keyword)

    warning_details = []

    for keyword in detected_warnings:
        warning_details.append({
            "keyword": keyword,
            "explanation": warning_explanations[keyword]
        })

        critical_keywords = [
        "share your otp",
        "send your password",
        "pay to get the job",
        "pay security deposit",
        "upfront payment"
    ]

    high_keywords = [
        "pay registration fee",
        "pay a registration fee",
        "registration fee required",
        "pay training fee",
        "processing fee",
        "application fee",
        "urgent payment required",
        "personal bank account"
    ]

    risk_score = 0

    for keyword in detected_warnings:
        if keyword in critical_keywords:
            risk_score += 25
        elif keyword in high_keywords:
            risk_score += 15
        else:
            risk_score += 8

    risk_score = min(risk_score, 100)

    if risk_score >= 60:
        risk_level = "High"
    elif risk_score >= 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "warnings": detected_warnings,
        "warning_details": warning_details,
        "message": "Analysis completed successfully"
    }
