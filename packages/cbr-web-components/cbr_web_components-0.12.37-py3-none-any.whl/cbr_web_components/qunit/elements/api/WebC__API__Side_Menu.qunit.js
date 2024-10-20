import WebC__Target_Div             from "../../../js/utils/WebC__Target_Div.mjs";
import Web_Component                from "../../../js/core/Web_Component.mjs";
import API__Invoke                  from "../../../js/data/API__Invoke.mjs";
import WebC__API__Side_Menu         from "../../../js/elements/api/WebC__API__Side_Menu.mjs";
import WebC__API_Markdown_To_Html   from "../../../js/elements/api/WebC__API_Markdown_To_Html.mjs";
import Load_Libraries__CSS          from "../../../js/utils/Load_Libraries__CSS.mjs";



QUnit.module('WebC__API__Side_Menu', function(hooks) {
    let target_div
    let webc__api_side_menu
    let mock_responses
    let api_path
    let data_file

    hooks.beforeEach(async (assert) =>{
        data_file                = WebC__API__Side_Menu.data_file__default_menu
        target_div               = WebC__Target_Div.add_to_body()
        mock_responses           = JSON.stringify(api_mock_data())
        let attributes           = {['disable-cdn']:'True', ['data-file']: data_file, mock_responses: mock_responses, api_path: api_path }
        webc__api_side_menu = await target_div.append_child(WebC__API__Side_Menu, attributes)
    })

    hooks.afterEach(() => {
        webc__api_side_menu.remove()
        target_div              .remove()
    })

    function api_mock_data() {
        const url__css__material_design_icons              = Load_Libraries__CSS.url__css__material_design_icons

        const  url__api__data_file = WebC__API__Side_Menu.url__api__data_file + WebC__API__Side_Menu.data_file__default_menu
        return { [url__api__data_file            ] : expected_menu_data      ,
                 [url__css__material_design_icons] : '.simple {css : "code"} ' }
    }

    QUnit.test('.constructor', (assert) => {
        const  url__api__data_file = WebC__API__Side_Menu.url__api__data_file + WebC__API__Side_Menu.data_file__default_menu
        assert.deepEqual(url__api__data_file, '/markdown/static_content/data-file?path=en/web-pages/dev/web-components/api/side-menu/side-menu-1.toml')
        assert.deepEqual(target_div.constructor.name                  , 'WebC__Target_Div'                            )
        assert.deepEqual(WebC__API__Side_Menu.name                    , 'WebC__API__Side_Menu'                   )
        assert.deepEqual(webc__api_side_menu.data_file                , data_file                                  )
        assert.deepEqual(webc__api_side_menu.getAttributeNames()      , ['disable-cdn', 'data-file', 'mock_responses', 'api_path'])
        assert.deepEqual(webc__api_side_menu.api_invoke.mock_responses, JSON.parse(mock_responses)                    )

        assert.ok       (WebC__API__Side_Menu.prototype          instanceof Web_Component              )
        assert.ok       (webc__api_side_menu                instanceof WebC__API_Markdown_To_Html )
        assert.ok       (webc__api_side_menu                instanceof Web_Component              )
        assert.ok       (webc__api_side_menu                instanceof HTMLElement                )
        assert.ok       (webc__api_side_menu.api_invoke     instanceof API__Invoke                )
        assert.ok       (webc__api_side_menu.css_load_result.css_loaded)
    })

    // todo: fix this test which started failing after adding the screenshot link (which has a dynamic link)
    // QUnit.test('.build', (assert) => {
    //     assert.deepEqual(webc__api_side_menu.inner_html(), expected_html    )
    // })

    QUnit.test('.load_menu_data', (assert) => {
        assert.deepEqual(webc__api_side_menu.menu_data, expected_menu_data)
    })

    const expected_menu_data = {
          'home'  : { 'href': 'home'  , 'icon': 'mdi-home' , 'text': 'Home'  , 'logged_in': false , 'visibility': true },
          'athena': { 'href': 'athena', 'icon': 'mdi-robot', 'text': 'Athena', 'logged_in': false , 'visibility': true },
      };
    const expected_html = `\
<div class="side_menu_section">
    <div class="side_menu_item">
        <a class="side_menu_link" href="${expected_menu_data.home.href}">
            <div class="mdi me-2 ${expected_menu_data.home.icon} side_menu_icon">
            </div>
            <div class="side_menu_text">${expected_menu_data.home.text}</div>
        </a>
    </div>
    <div class="side_menu_item">
        <a class="side_menu_link" href="${expected_menu_data.athena.href}">
            <div class="mdi me-2 ${expected_menu_data.athena.icon} side_menu_icon">
            </div>
            <div class="side_menu_text">${expected_menu_data.athena.text}</div>
        </a>
    </div>    
</div>
`


})