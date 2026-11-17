
from urllib.parse import urlparse
import ipaddress


def analyze_url(url: str):
    """
    Analyse a website URL and identify possible phishing warning signs.
    """

    warnings = []
    warning_details = []
    risk_score = 0

    # Step 1: Clean and parse the URL
    url = url.strip()
    parsed_url = urlparse(url)

    # Add HTTPS if the user does not provide a scheme
    if not parsed_url.scheme:
        url = "https://" + url
        parsed_url = urlparse(url)

    hostname = parsed_url.hostname

    # Step 2: Validate the URL
    if not hostname or parsed_url.scheme not in ["http", "https"]:
        return {
            "risk_score": 0,
            "risk_level": "Unknown",
            "warnings": ["Invalid URL"],
            "warning_details": [],
            "message": "Please provide a valid website URL."
        }

    hostname = hostname.lower()

    # Step 3: Check HTTP instead of HTTPS
    if parsed_url.scheme == "http":
        warnings.append("No HTTPS encryption")
        warning_details.append({
            "keyword": "HTTP",
            "explanation": "This website uses HTTP instead of HTTPS. Data sent to it may not be encrypted."
        })
        risk_score += 15

    # Step 4: Check whether the hostname is an IP address
    try:
        ipaddress.ip_address(hostname)

        warnings.append("IP address used as domain")
        warning_details.append({
            "keyword": hostname,
            "explanation": "The website uses an IP address instead of a normal domain name. This deserves additional verification."
        })
        risk_score += 25

    except ValueError:
        pass

    # Step 5: Check suspicious words in both hostname and URL path
    suspicious_words = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "bonus",
        "free"
    ]

    searchable_url = (hostname + parsed_url.path).lower()

    for word in suspicious_words:
        if word in searchable_url:
            warnings.append(f"Suspicious word: {word}")

            warning_details.append({
                "keyword": word,
                "explanation": f"The URL contains the word '{word}'. This may require additional verification."
            })

            risk_score += 8

    # Step 6: Check for too many subdomains
    domain_parts = hostname.split(".")

    if len(domain_parts) > 4:
        warnings.append("Excessive subdomains")

        warning_details.append({
            "keyword": hostname,
            "explanation": "The domain contains many subdomains, which can make the actual website owner harder to identify."
        })

        risk_score += 15

    # Step 7: Check excessive hyphens
    if hostname.count("-") >= 3:
        warnings.append("Excessive hyphens in domain")

        warning_details.append({
            "keyword": hostname,
            "explanation": "The domain contains several hyphens. This can sometimes be used in deceptive domain names."
        })

        risk_score += 10

    # Step 8: Check for punycode domains
    if "xn--" in hostname:
        warnings.append("Punycode domain detected")

        warning_details.append({
            "keyword": hostname,
            "explanation": "This domain uses encoded characters and should be checked for possible lookalike characters."
        })

        risk_score += 20

    # Step 9: Calculate final risk score
    risk_score = min(risk_score, 100)

    if risk_score >= 60:
        risk_level = "High"
    elif risk_score >= 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # Step 10: Return analysis result
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "warnings": warnings,
        "warning_details": warning_details,
        "message": "URL analysis completed successfully"
    }
