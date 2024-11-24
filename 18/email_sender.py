import yagmail
from typing import List, Union, Optional, Dict
from jinja2 import Environment, FileSystemLoader

# pip install yagmail, keyring, jinja2

class EmailSender:
    def __init__(self, passcode: str, sender: Optional[str] = None, ):
        """
        Initialize the EmailSender with an optional sender email.
        """
        self.sender = sender
        self.yag = yagmail.SMTP(sender, passcode)
    
    def read_template(self, template_path: str) -> str:
        """
        Reads the HTML template from a given file path.
        """
        try:
            with open(template_path, 'r', encoding='utf-8') as template_file:
                return template_file.read()
        except FileNotFoundError:
            raise ValueError(f"Template file '{template_path}' not found.")
    
    def render_template(self, template_str: str, params: Dict[str, str]) -> str:
        """
        Renders the template with Jinja2 using the provided parameters.
        """
        env = Environment(loader=FileSystemLoader('.'))  # Current directory for file loading
        template = env.from_string(template_str)
        return template.render(params)
    
    def send_email(
        self,
        to: Union[str, List[str]],
        subject: str,
        body: Union[str, Dict[str, str]],
        attachments: Union[str, List[str]] = None
    ):
        """
        Sends an email. Handles both plain text and HTML email content.
        """
        try:
            # Process body for HTML emails
            if isinstance(body, dict):  # Dictionary implies HTML content
                if 'html_template_path' not in body or 'params' not in body:
                    raise ValueError("For HTML emails, 'body' must include 'html_template_path' and 'params'.")
                
                template_str = self.read_template(body['html_template_path'])
                html_content = self.render_template(template_str, body['params'])
                
                # Optional plain text fallback
                text_content = body.get('text', "This email requires an HTML-capable client.")
                body_content = [text_content, yagmail.inline(html_content)]
            else:
                body_content = body  # Plain text email
            
            # Send the email
            self.yag.send(
                to=to,
                subject=subject,
                contents=body_content,
                attachments=attachments
            )
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
