# Instagram Direct Messages API 

## Example:

```python
from typing import List

from instagram_direct import InstagramDirect
from instagram_direct.direct_api.model.MessageModel import MessageModel

direct = InstagramDirect(session_id="your_session_id")

async def main():
    all_threads = await direct.inbox.all()
    all_new_threads = await direct.inbox.all_pending()
    
    selected_thread = await direct.thread.get("thread_id", cursor="for previus pages")
    
    chat_messages: List[MessageModel] = selected_thread.messages
    
    unread_count: int = await direct.badge.unread_count()

```

## Direct API Endpoints:

- [x] /api/v1/direct_v2/inbox/
- [x] /api/v1/direct_v2/pending_inbox/
- [x] /api/v1/direct_v2/threads/<thread_id:int>/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/items/<item_id:int>/seen/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/items/<item_id:int>/delete/
- [ ] /api/v1/direct_v2/threads/approve_multiple/
- [ ] /api/v1/direct_v2/threads/decline_all/
- [ ] /api/v1/direct_v2/threads/decline_multiple/
- [ ] /api/v1/direct_v2/threads/broadcast/configure_photo/
- [ ] /api/v1/direct_v2/ranked_recipients/
- [ ] /api/v1/direct_v2/create_group_thread/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/add_user/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/remove_users/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/add_admins/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/remove_admins/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/update_title/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/mute_video_call/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/unmute_video_call/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/mute/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/unmute/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/leave/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/hide/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/move/
- [ ] /api/v1/direct_v2/threads/broadcast/reel_share/
- [ ] /api/v1/direct_v2/threads/broadcast/story_share/
- [ ] /api/v1/direct_v2/threads/broadcast/live_viewer_invite/
- [ ] /api/v1/direct_v2/threads/broadcast/link/
- [ ] /api/v1/direct_v2/threads/broadcast/reel_react/
- [x] /api/v1/direct_v2/get_badge_count/
- [ ] /api/v1/direct_v2/get_presence/
- [ ] /api/v1/direct_v2/threads/broadcast/forward/
- [ ] /api/v1/direct_v2/has_interop_upgraded/
- [ ] ~~/api/v1/direct_v2/threads/<thread_id:int>/get_items/~~
- [ ] /api/v1/direct_v2/icebreakers/get_suggested_icebreakers/
- [ ] /api/v1/direct_v2/threads/<thread_id:int>/set_disappearing_messages_settings/
- [ ] /api/v1/users/web_profile_info/


### Supported 4/35 Endpoints

---

# Внимание:

### Автор/ы кода не несут ответственности если ваш аккаунт заблокируют или получит ограничения
