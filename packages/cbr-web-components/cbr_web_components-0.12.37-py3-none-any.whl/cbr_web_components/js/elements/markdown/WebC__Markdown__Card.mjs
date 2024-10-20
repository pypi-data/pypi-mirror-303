import A                          from "../../core/A.mjs";
import Div                        from "../../core/Div.mjs";
import WebC__API_Markdown_To_Html from "../api/WebC__API_Markdown_To_Html.mjs";

export default class WebC__Markdown__Card extends WebC__API_Markdown_To_Html {

    static class__card           = 'markdown_card';
    static class__card_body      = 'markdown_card_body';
    static class__card_title     = 'markdown_card_title';
    static class__card_subtitle  = 'markdown_card_subtitle';
    static class__content_div    = 'markdown_content_div';
    static class__action         = 'markdown_action';
    static class__action_link    = 'markdown_action_link';

    async build() {
        const div_card        = new Div({ class: WebC__Markdown__Card.class__card           });                     // Create individual Div components for the card structure
        const div_card_body   = new Div({ class: WebC__Markdown__Card.class__card_body      });
        const div_title       = new Div({ class: WebC__Markdown__Card.class__card_title     });
        const div_sub_title   = new Div({ class: WebC__Markdown__Card.class__card_subtitle  });
        const div_content     = new Div({ class: WebC__Markdown__Card.class__content_div    });
        const div_action      = new Div({ class: WebC__Markdown__Card.class__action         });                     // Create a div for the button (action button)


        const action_href     = this.markdown_metadata.action_link
        const action_text     = this.markdown_metadata.action_text || 'Go'
        const a_action        = new A({ class: WebC__Markdown__Card.class__action_link, value: this.markdown_metadata.action_text , attributes: { href: action_href } });

        div_title    .value = this.markdown_metadata.title     || '';                                               // Set values from the Markdown metadata and content
        div_sub_title.value = this.markdown_metadata.sub_title || '';
        div_content  .value = this.markdown_html               || '';

        if (this.markdown_metadata.title     ) { div_card_body.add_element(div_title     ); }                       // Add metadata elements to the card body
        if (this.markdown_metadata.sub_title ) { div_card_body.add_element(div_sub_title ); }

        div_action   .add_element(a_action     );                                                                   // Add the action button to the card body
        div_card_body.add_element(div_content  );                                                                   // Add content section to the card body
        div_card_body.add_element(div_action   );                                                                   // Add action button to the card body
        div_card     .add_element(div_card_body);                                                                   // Assemble the card structure

        const html = div_card.html();                                                                               // Convert to HTML and set as inner content of the component
        this.set_inner_html(html);
    }


    css_rules() {
        return {
            [`.${WebC__Markdown__Card.class__card}`                   ] : {  'display'          : 'inline-block'         ,
                                                                             'padding'          : '0px'                 ,
                                                                             'height'           : '100%'                ,
                                                                             'width'            : '100%'                ,
                                                                             'margin'           : '0px'                ,
                                                                             'vertical-align'   : 'top'                 },
            [`.${WebC__Markdown__Card.class__card_body}`              ] : {  'display'          : 'flex'                 ,  // Enable flexbox layout
                                                                             'flex-direction'   : 'column'              ,  // Arrange items in a column
                                                                             'justify-content'  : 'space-between'       ,  // Space out elements vertically
                                                                             'background-color' : '#fff'                ,
                                                                             'border'           : '1px solid #ddd'      ,
                                                                             'padding'          : '10px'                ,
                                                                             'border-radius'    : '8px'                 ,
                                                                             'height'           : '100%'                ,
                                                                             'box-sizing'       : 'border-box'          },
            [`.${WebC__Markdown__Card.class__card_title}`             ] : {  'font-size'        : '21px'                 ,
                                                                             'font-weight'      : '400'                 ,
                                                                             'margin-bottom'    : '0.75rem'             },
            [`.${WebC__Markdown__Card.class__card_subtitle}`          ] : {  'font-weight'      : '300'                  ,
                                                                             'color'            : '#99abb4'             ,
                                                                             'margin-bottom'    : '6px'                 },
            [`.${WebC__Markdown__Card.class__content_div}`            ] : {  'width'            : '100%'                 ,
                                                                             'position'         : 'relative'            ,
                                                                             'overflow'         : 'auto'                ,
                                                                             'line-height'      : '1.5'                 ,
                                                                             'flex-grow'        : '1'                   },  // Make the content div take up remaining space
            [`.${WebC__Markdown__Card.class__content_div} a`          ] : {  'color'            : '#007bff'              ,
                                                                             'text-decoration'  : 'none'                },
            [`.${WebC__Markdown__Card.class__content_div} a:hover`    ] : {  'text-decoration'  : 'underline'            },
            [`.${WebC__Markdown__Card.class__content_div} .btn`       ] : {  'margin-top'       : '10px'                 },
            [`.${WebC__Markdown__Card.class__action}`                 ] : {  'display'          : 'flex'                 ,  // Use flexbox for button alignment
                                                                             'justify-content'  : 'center'              ,  // Center the button horizontally
                                                                             'align-self'       : 'flex-center'            ,  // Align the button at the bottom
                                                                             'margin-top'       : '10px'                },  // Ensure some spacing above the button
            [`.${WebC__Markdown__Card.class__action_link}`            ] : {  'background-color' : '#26c6da'              ,
                                                                             'color'            : '#fff'                ,
                                                                             'padding'          : '5px 20px'           ,
                                                                             'border-radius'    : '4px'                 ,
                                                                             'text-decoration'  : 'none'                ,
                                                                             'font-size'        : '14px'                ,
                                                                             'display'          : 'inline-block'        ,
                                                                             'transition'       : 'background-color 0.3s' },
            [`.${WebC__Markdown__Card.class__action_link}:hover`      ] : {  'background-color' : '#1d9ca9'              }
        };
    }
}

WebC__Markdown__Card.define()