import WebC__Target_Div      from "../../../js/utils/WebC__Target_Div.mjs";
import WebC__Server_Requests from "../../../js/elements/ui/WebC__Server_Requests.mjs";
import Web_Component         from "../../../js/core/Web_Component.mjs";
import API__Invoke           from "../../../js/data/API__Invoke.mjs";
import WebC__API_To_Table from "../../../js/elements/api/WebC__API_To_Table.mjs";
import Table from "../../../js/core/Table.mjs";

QUnit.module('WebC__Server_Requests', function(hooks) {
    let target_div
    let webc_server_requests
    let mock_responses
    let api_path
    let api_data

    hooks.beforeEach(async (assert) => {
        api_path            = '/an/path/to/load'
        api_data            = {'headers': ['requests_ids'], 'rows': [['2', 'a'], [2, 'b'], [3, 'c']], 'title':'an table'}
        mock_responses      = JSON.stringify({[api_path]: api_data})
        target_div          = WebC__Target_Div.add_to_body().build()
        let attributes      = { mock_responses: mock_responses, api_path: api_path}
        webc_server_requests   = await target_div.append_child(WebC__Server_Requests, attributes)
        await webc_server_requests.wait_for_event('build-complete')
    })

    hooks.afterEach(() => {
        webc_server_requests.remove()
        target_div.remove()
    })

    QUnit.test ('.constructor', (assert) => {
        assert.deepEqual(WebC__Server_Requests.name, 'WebC__Server_Requests')
        assert.ok(WebC__Server_Requests.prototype instanceof WebC__API_To_Table)
        assert.ok(WebC__Server_Requests.prototype instanceof Web_Component)
        assert.ok(webc_server_requests instanceof Web_Component)
        assert.ok(webc_server_requests instanceof HTMLElement)
        assert.ok(webc_server_requests.api_invoke instanceof API__Invoke)
        assert.deepEqual(webc_server_requests.getAttributeNames(), ['mock_responses', 'api_path'])

        assert.deepEqual(webc_server_requests.api_invoke.mock_responses, JSON.parse(mock_responses))
        assert.deepEqual(webc_server_requests.api_path, api_path)
    })

    QUnit.test ('.build', (assert) => {
        let table = new Table()
        table.headers = api_data['headers']
        table.rows    = api_data['rows']
        let expected_html = `\
<div id="api_to_table">
    <a id="data_reload" href="#reload">reload</a>
${table.html(1)}\
</div>
`;
        // let expected_html = "<div id=\"api_to_table\">\n"+
        //                     "    <a id=\"data_reload\" href=\"#reload\">reload</a>\n" +
        //                          table.html(1) +
        //                     "</div>\n"
        assert.deepEqual(webc_server_requests.inner_html(), expected_html)

    })
})