import WebC__Target_Div             from "../../../js/utils/WebC__Target_Div.mjs";
import Web_Component                from "../../../js/core/Web_Component.mjs";
import API__Invoke                  from "../../../js/data/API__Invoke.mjs";
import WebC__API_Markdown_To_Html   from "../../../js/elements/api/WebC__API_Markdown_To_Html.mjs";
import WebC__Markdown__Card         from "../../../js/elements/markdown/WebC__Markdown__Card.mjs";



QUnit.module('WebC__Markdown__Card', function(hooks) {
    let target_div
    let webc__markdown_card
    let mock_responses
    let api_path
    let content_path

    hooks.beforeEach(async (assert) =>{
        content_path               = 'en/web-pages/demos/index.md'
        target_div                 = WebC__Target_Div.add_to_body()
        mock_responses             = JSON.stringify(api_mock_data())
        let attributes             = { ['disable-cdn']:'True', ['content-path']:content_path, mock_responses: mock_responses, api_path: api_path }
        webc__markdown_card        = await target_div.append_child(WebC__Markdown__Card, attributes)
    })

    hooks.afterEach(() => {
        webc__markdown_card.remove()
        target_div         .remove()
    })

    function api_mock_data() {
        const url__api_markdown_file_to_html_and_metadata  = WebC__Markdown__Card.url__api_markdown_file_to_html_and_metadata + content_path
        const data__api_markdown_file_to_html_and_metadata = {'html': expected_raw_html, metadata: expected_metadata}
        return { [url__api_markdown_file_to_html_and_metadata]: data__api_markdown_file_to_html_and_metadata }
    }



    QUnit.test('.constructor', (assert) => {
        assert.deepEqual(target_div.constructor.name                  , 'WebC__Target_Div'                            )
        assert.deepEqual(WebC__Markdown__Card.name                    , 'WebC__Markdown__Card'                        )
        assert.deepEqual(webc__markdown_card.content_path             , content_path                                  )
        assert.deepEqual(webc__markdown_card.getAttributeNames()      , ['disable-cdn', 'content-path', 'mock_responses', 'api_path'])
        assert.deepEqual(webc__markdown_card.api_invoke.mock_responses, JSON.parse(mock_responses)                    )

        assert.ok       (WebC__Markdown__Card.prototype      instanceof Web_Component            )
        assert.ok       (webc__markdown_card                instanceof WebC__API_Markdown_To_Html)
        assert.ok       (webc__markdown_card                instanceof Web_Component             )
        assert.ok       (webc__markdown_card                instanceof HTMLElement               )
        assert.ok       (webc__markdown_card.api_invoke     instanceof API__Invoke               )
    })

    QUnit.test('.build', (assert) => {
        assert.deepEqual(webc__markdown_card.inner_html(), expected_html    )
    })

    const expected_raw_html = `<h1>Markdown content</h1><ul><li>will go here</li></ul>`
    const expected_metadata = { 'title': 'Markdown content' ,
                                'sub_title': 'will go here' ,
                                'action_link': 'some/page'  ,
                                'action_text': 'Go to page' }
    const expected_html = `\
<div class="markdown_card">
    <div class="markdown_card_body">
        <div class="markdown_card_title">${expected_metadata.title}</div>
        <div class="markdown_card_subtitle">${expected_metadata.sub_title}</div>
        <div class="markdown_content_div">${expected_raw_html}</div>
        <div class="markdown_action">
            <a class="markdown_action_link" href="${expected_metadata.action_link}">${expected_metadata.action_text}</a>
        </div>
    </div>
</div>
`
})
