import WebC__API_Markdown_To_Html   from "../../../js/elements/api/WebC__API_Markdown_To_Html.mjs";
import Web_Component                from "../../../js/core/Web_Component.mjs";
import API__Invoke                  from "../../../js/data/API__Invoke.mjs";
import WebC__Target_Div             from "../../../js/utils/WebC__Target_Div.mjs";

QUnit.module('WebC__API_Markdown_To_Html', function(hooks) {
    let target_div
    let webc__api_markdown_to_html
    let mock_responses
    let api_path
    let content_path

    hooks.beforeEach(async (assert) =>{
        content_path               = 'en/web-pages/demos/index.md'
        target_div                 = WebC__Target_Div.add_to_body()
        mock_responses             = JSON.stringify(api_mock_data())
        let attributes             = { ['disable-cdn']:'True', ['content-path']:content_path, mock_responses: mock_responses, api_path: api_path }
        webc__api_markdown_to_html = await target_div.append_child(WebC__API_Markdown_To_Html, attributes)
    })

    function api_mock_data() {
        const url__api_markdown_file_to_html_and_metadata  = WebC__API_Markdown_To_Html.url__api_markdown_file_to_html_and_metadata + content_path
        const data__api_markdown_file_to_html_and_metadata = {'html': expected_raw_html, metadata: expected_metadata}
        return { [url__api_markdown_file_to_html_and_metadata]: data__api_markdown_file_to_html_and_metadata }
    }
    hooks.afterEach(() => {
        webc__api_markdown_to_html.remove()
        target_div                .remove()
    })

    QUnit.test('.constructor', (assert) => {
        assert.deepEqual(target_div.constructor.name                         , 'WebC__Target_Div'                            )
        assert.deepEqual(WebC__API_Markdown_To_Html.name                     , 'WebC__API_Markdown_To_Html'                  )
        assert.deepEqual(webc__api_markdown_to_html.content_path             , content_path                                  )
        assert.deepEqual(webc__api_markdown_to_html.getAttributeNames()      , ['disable-cdn', 'content-path', 'mock_responses', 'api_path'])
        assert.deepEqual(webc__api_markdown_to_html.api_invoke.mock_responses, JSON.parse(mock_responses)                    )

        assert.ok       (WebC__API_Markdown_To_Html.prototype      instanceof Web_Component     )
        assert.ok       (webc__api_markdown_to_html                instanceof Web_Component     )
        assert.ok       (webc__api_markdown_to_html                instanceof HTMLElement       )
        assert.ok       (webc__api_markdown_to_html.api_invoke     instanceof API__Invoke       )
    })

    QUnit.test('.build', (assert) => {
        assert.deepEqual(webc__api_markdown_to_html.markdown_html          , expected_raw_html    )
        assert.deepEqual(webc__api_markdown_to_html.shadow_root().innerHTML, expected_html    )
    })

    QUnit.test('static.on_error_return_value', async (assert) => {
        assert.deepEqual(webc__api_markdown_to_html.content_path, content_path)
        await webc__api_markdown_to_html.load_html_content_and_metadata()
        assert.deepEqual(webc__api_markdown_to_html.markdown_html    , expected_raw_html)
        assert.deepEqual(webc__api_markdown_to_html.markdown_metadata, expected_metadata)

        webc__api_markdown_to_html.content_path = 'aaaa/bbbb/cccc.md'
        await webc__api_markdown_to_html.load_html_content_and_metadata()
        assert.deepEqual(webc__api_markdown_to_html.markdown_html    , WebC__API_Markdown_To_Html.on_error_return_value.html    )
        assert.deepEqual(webc__api_markdown_to_html.markdown_metadata, WebC__API_Markdown_To_Html.on_error_return_value.metadata)
    })
    const expected_raw_html = `<h1>Markdown content</h1><ul><li>will go here</li></ul>`
    const expected_metadata = { 'title': 'Markdown content' , 'sub_title': 'will go here', 'description': 'an description' , 'error': 'an error'}
    const expected_html = `\
<div class="markdown_section">
    <div class="markdown_metadata">
        <div class="markdown_error">an error</div>
        <div class="markdown_title">Markdown content</div>
        <div class="markdown_sub_title">will go here</div>
        <div class="markdown_description">an description</div>
    </div>
    <div class="markdown_html"><h1>Markdown content</h1><ul><li>will go here</li></ul></div>
</div>
`
})

