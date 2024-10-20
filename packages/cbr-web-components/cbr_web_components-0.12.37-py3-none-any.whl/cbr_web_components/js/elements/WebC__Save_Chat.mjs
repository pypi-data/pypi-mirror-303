import Web_Component from "../core/Web_Component.mjs";
import Tag from "../core/Tag.mjs";

export default class WebC__Save_Chat extends Web_Component {

    constructor() {
        super();
        this.chat_thread_id = null
    }

    connectedCallback() {
        this.build()
    }

    build() {
        this.set_inner_html(this.html())
    }

    html() {
        const div__save_chat         = new Tag({tag: 'div'  , id: 'save_chat'})
        const button__share          = new Tag({tag:'button', id: 'button_share' , value: 'Share'})
        const label__chat_thread_id  = new Tag({tag:'label' , id: 'chat_thread_id' , value: '....'})
        div__save_chat.add(button__share)
        div__save_chat.add(label__chat_thread_id)
        return div__save_chat.html()
    }
}

WebC__Save_Chat.define()