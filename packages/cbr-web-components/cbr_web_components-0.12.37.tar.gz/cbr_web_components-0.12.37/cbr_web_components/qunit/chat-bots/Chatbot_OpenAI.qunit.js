import Chatbot_OpenAI   from '../../js/chat-bots/Chatbot_OpenAI.mjs'
import Web_Component    from '../../js/core/Web_Component.mjs'
import WebC__Target_Div from "../../js/utils/WebC__Target_Div.mjs";

QUnit.module('Chatbot_OpenAI', function(hooks) {

    let chatbot_openai
    let target_div
    let div_system_prompt

    hooks.before((assert) => {
        target_div                      = WebC__Target_Div.add_to_body().build({width: "50%"})
        chatbot_openai                  = target_div.append_child(Chatbot_OpenAI)

        div_system_prompt                 = document.createElement('div');                // todo: find a better way to add this temp DIV
        div_system_prompt.id              = 'system_prompt';
        div_system_prompt.style.display   = 'none';
        document.body.appendChild(div_system_prompt);
        assert.equal(document.body.querySelector('#system_prompt').outerHTML, '<div id="system_prompt" style="display: none;"></div>')

    });

    hooks.beforeEach(() => {
        chatbot_openai.messages.messages_clear()
    })

    hooks.afterEach(() => {

    })

    hooks.after((assert) => {
        assert.equal(chatbot_openai.messages.messages_size(),0)
        target_div.remove()
        div_system_prompt.remove()
    })

    QUnit.test('constructor', (assert) => {
        assert.ok(true)
        assert.ok(Chatbot_OpenAI.prototype instanceof Web_Component);
        assert.deepEqual(chatbot_openai.stop_fetch, false)
    })

    QUnit.test('add_thread_id_ui_link', (assert) => {
        assert.equal(chatbot_openai.messages.messages_size(),0)

        chatbot_openai.add_thread_id_ui_link()

        assert.equal(chatbot_openai.messages.messages_size(),1)
        let last_message = chatbot_openai.messages.messages()[0]
        let chat_thread_id = chatbot_openai.chat_thread_id
        let last_message_inner_html = `<a style="padding:0px" href="chat/view/${chat_thread_id}" target="_blank">view saved chat</a>`
        assert.deepEqual(last_message.innerHTML, last_message_inner_html)
    })

    QUnit.test('all_system_prompts', (assert) => {

        assert.deepEqual(chatbot_openai.all_system_prompts(), [])

        chatbot_openai.system_prompt = 'an system_prompt'
        assert.deepEqual(chatbot_openai.all_system_prompts(), ['an system_prompt'])

        chatbot_openai.system_prompt = null

        div_system_prompt.innerHTML = 'this is another system prompt'
        assert.deepEqual(chatbot_openai.all_system_prompts(), ['this is another system prompt'])
        div_system_prompt.innerHTML = ''
        assert.deepEqual(chatbot_openai.all_system_prompts(), [])
    })

    QUnit.test('apply_ui_tweaks', (assert) => {
        assert.deepEqual(chatbot_openai.all_system_prompts(), [])
        assert.equal(chatbot_openai.input.value   , '')
        assert.equal(chatbot_openai.initial_prompt, '')
        chatbot_openai.apply_ui_tweaks()
        assert.equal(chatbot_openai.input.value, '')

        chatbot_openai.initial_prompt = 'an initial prompt'
        chatbot_openai.apply_ui_tweaks()
        assert.equal(chatbot_openai.input.value, 'an initial prompt')

        chatbot_openai.initial_message = 'an initial message'
        chatbot_openai.apply_ui_tweaks()

        assert.deepEqual(chatbot_openai.messages.messages_size(),1)
        assert.deepEqual(chatbot_openai.messages.messages()[0].outerHTML, '<webc-chat-message type="initial" style="display: inherit;">an initial message</webc-chat-message>')

        chatbot_openai.messages.messages_clear()
        chatbot_openai.initial_message = null

        chatbot_openai.system_prompt = 'an system prompt'
        chatbot_openai.apply_ui_tweaks()
        assert.deepEqual(chatbot_openai.messages.messages_size(),1)
        assert.deepEqual(chatbot_openai.messages.messages()[0].outerHTML, '<webc-chat-message type="system" style="display: inherit;">an system prompt</webc-chat-message>')

        chatbot_openai.messages.messages_clear()
    })



    QUnit.test('post_openai_prompt_with_stream', async (assert) => {

        const fake_fetch_request_post = async (url, body) => {
            return {
                ok      : true    ,
                status  : 200     ,
                body    : { getReader() { return { read() {return Promise.resolve({ done: true,
                                                                                    value: new TextEncoder().encode('{"message": "fake data"}' )})}}}}
            };
        }
        chatbot_openai.fetch_request_post = fake_fetch_request_post

        const done          = assert.async();

        const end_test = () => {
            chatbot_openai.messages.messages_clear()
            done()
        }

        const user_prompt = '2+2'
        const images      = null

        chatbot_openai.addEventListener('streamComplete', function(event) {
            assert.deepEqual(event.detail, null)
            end_test();
            }, { once: true });

        chatbot_openai.post_openai_prompt_with_stream(user_prompt, images)
    });

    //     chatbot_openai.addEventListener('streamData', function(event) {
    //         console.log('in streamData')
    //         const expected_data = { channel: null, data: 'HTTP error! Status: 404' }
    //         //assert.deepEqual(event.detail, expected_data)
    //         end_test();
    //         }, { once: true });
})