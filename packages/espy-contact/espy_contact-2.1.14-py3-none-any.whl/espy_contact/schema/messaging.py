"""Copyright 2024 Everlasting Systems and Solutions LLC (www.myeverlasting.net).
All Rights Reserved.

No part of this software or any of its contents may be reproduced, copied, modified or adapted, without the prior written consent of the author, unless otherwise indicated for stand-alone materials.

For permission requests, write to the publisher at the email address below:
office@myeverlasting.net

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from pydantic import BaseModel,EmailStr,field_serializer,field_validator
from datetime import datetime
import base64
import binascii
from espy_contact.util.enums import ChannelEnum
class MessageCreate(BaseModel):
    sender_id: int
    recipient_type: ChannelEnum
    recipient_id: int
    content: dict 

    @field_validator('content', mode='before')
    def validate_content(cls, content: dict):
        if not content:
            raise ValueError('Content cannot be empty')
        if not isinstance(content, dict):
            raise ValueError('Content must be a dictionary')
        if 'subject' not in content or content['subject'] == '':
            raise ValueError('Content must have a subject')
        if 'message' not in content or content['message'] == '':
            raise ValueError('Content must have a message')
        return content
    class Config:
        json_schema_extra = {
            "example": {
                "sender_id": 1,
                "recipient_type": ChannelEnum.SCHOOL,
                "recipient_id": 2,
                "event_type": "School Holiday",
                "content": {
                    "subject": "Test",
                    "message": "This is a test message"
                }
            }
        }


class MessageResponse(MessageCreate):
    updated_at: datetime
    id: int

    @field_serializer('updated_at')
    def serialize_updated_at(self, updated_at: datetime):
        return updated_at.isoformat()

class AttachmentDto(BaseModel):
    filename: str
    content: str # base64 encoded
    mime_type: str | None = None

    @field_validator('content')
    def validate_content(cls, content: str):
        if not content:
            raise ValueError('Content cannot be empty')
        try:
            base64.b64decode(content, validate=True)
        except binascii.Error as e:
            raise ValueError('Content must be base64 encoded')
        return content
    
class MailerDto(BaseModel):
    recipients: list[EmailStr]
    name: str | None = None
    subject: str
    message: str
    created_at: datetime | None = datetime.now()
    is_html: bool | None = False
    attachments: list[AttachmentDto] | None = None
class Notification(MessageCreate):
    event_type: str
    created_at: datetime | None = datetime.now()