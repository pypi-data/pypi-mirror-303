//import '../../plugins/jquery/dist/jquery.min.mjs'
//import '../../plugins/data-tables/js/dataTables.min.mjs'
import Tag                from "../core/Tag.mjs"          ;
import Table              from "../core/Table.mjs";
import Div                from "../core/Div.mjs"          ;
import Web_Component      from "../core/Web_Component.mjs";

export default class WebC__Events_Viewer extends Web_Component {    

    constructor() {
        super();
        this.channels.push('WebC__Events_Viewer')
        this.events_to_hook  = ['channel_message', 'stop_stream', 'messageSent', 'new_input_message', 'streamStart', 'streamData','streamComplete','streamError']
        this.events_hooked   = []  
        this.events_handled = []
        this.on_event        = this.on_event.bind(this);
        this.data_table      = null
        this.index           = 0
    }

    add_row(row) {
        if (row) {
            //this.data_table.row.add(row).draw()
              this.data_table.row.add(row.map(String)).draw(); // Convert all elements to strings

        }
    }
        
    build() {
        this.set_inner_html(this.render_html() )
        this.add_css_rules (this.css_rules  () )
        this.set_data_table()
        this.hook_events   (this.events_to_hook)
        
    }

    connectedCallback() {
        this.build()
    }

    css_rules() { return { '*'              : { "font-family"     : "Verdana"  },
                            '.event_viewer' : { "margin"          : "0px"      ,
                                                "border"          : "2px solid" ,
                                                'padding'         : '10px'      ,
                                                'background-color': '#FCFCF0'  }}
    }

    set_data_table() {
        let columns    =  [{ width: "10px"}, { }, {},  {width: "80%" }]

        //let columnDefs =  [{ className: "dt-center", targets: "_all" }]
        let config = {  columns    : columns ,
                        //columnDefs : columnDefs,
                        dom        : '<"top"f>rt<"bottom"i><"clear">'   ,
                        order      : [[0, 'desc']]                      }
        let table       = this.shadowRoot.querySelector('#target')
        this.data_table = $(table).DataTable(config)
    }

    render_html() {
        let events_viewer = new Div({class:'event_viewer'})
        let table         = new Table({id:'target'})
        table.headers     = ['#', 'event_type', 'channel', 'event_data']
        events_viewer.add_tag({tag:'h2', value:'Events Viewer'})
        events_viewer.add_element(table)
        let html = events_viewer.html()

        //todo: find a better way to add this css to the shadowRoot
        //html += `<style>@import url('/assets/plugins/data-tables/css/dataTables.dataTables.min.css');</style>`
        html += `
<style>
  

  table.dataTable td {    
    overflow: hidden;
    text-overflow: ellipsis;
    
  }


</style>        
`
        return html
    }

    on_event(event) {
        this.events_handled.push(event)
        let event_type = event.type
        let event_data = JSON.stringify(event.detail)
        let channel = event.detail?.channel
        this.add_row([this.index.toString(), event_type,channel, event_data])
        this.index++
    }

    hook_events(event_types, options) {
        if (event_types) {
            event_types.forEach(type => {
                document.addEventListener(type, this.on_event, options);
                this.events_hooked.push(type)
            })
        }
    }
}


WebC__Events_Viewer.define()

window.send_event = (message) => {
    let event_name = 'test-event'
    let event = new CustomEvent(event_name, {             
        detail    : { message:  message },      // Custom data to pass with the event
        bubbles   : true,                       // Whether the event bubbles up through the DOM
        cancelable: true,                       // Whether the event can be canceled
        composed  : false   ,                   // Whether the event will trigger listeners outside of a shadow root            
    }); 
    document.dispatchEvent(event)
}