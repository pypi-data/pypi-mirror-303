import WebC__Target_Div from "../../js/utils/WebC__Target_Div.mjs";
import Web_Component    from '../../js/core/Web_Component.mjs'
import WebC__Save_Chat from "../../js/elements/WebC__Save_Chat.mjs";

QUnit.module('WebC__Save_Chat', function(hooks) {

    let webc_save_chat
    let target_div
    let target_div_setup

    hooks.before(async (assert) => {
        target_div_setup = {right:"50px", top:"250px", width: "500px", height:"100px"}
        target_div       = WebC__Target_Div.add_to_body().build(target_div_setup)
        webc_save_chat   = target_div.append_child(WebC__Save_Chat)
    });


    QUnit.test('build', (assert) => {
        const expected_html = `\
<div id="save_chat">
    <button id="button_share">Share</button>
    <label id="chat_thread_id">....</label>
</div>
`
        //console.log(webc_save_chat.shadow_root().innerHTML)
        assert.equal(webc_save_chat.shadow_root().innerHTML, webc_save_chat.inner_html())
        assert.equal(webc_save_chat.inner_html() , expected_html)
        assert.ok(1)
    })

    QUnit.test('constructor', (assert) => {
        assert.ok(WebC__Save_Chat.prototype instanceof Web_Component, 'WebC__Save_Chat.prototype is an instance of Web_Component');assert.ok       (webc_save_chat instanceof Web_Component     , 'webc_save_chat is an instance of Web_Component')
        assert.deepEqual(webc_save_chat.channels, [ 'Web_Component' ], 'webc_save_chat.channels == [ "Web_Component" ]')
        assert.deepEqual(webc_save_chat.chat_thread_id, null         , 'webc_save_chat.chat_thread_id == null')
        window.webc_save_chat = webc_save_chat
    })


})