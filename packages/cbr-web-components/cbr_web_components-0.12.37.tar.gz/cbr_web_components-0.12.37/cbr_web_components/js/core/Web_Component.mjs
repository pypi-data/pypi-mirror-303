import Events__Utils from "../events/Events__Utils.mjs";

export default class Web_Component extends HTMLElement {

    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.channel   = null
        this.channels  = ['Web_Component']
        this.webc_id   = null
        this.webc_type = 'Web_Component'            // todo: see if this is useful
        this.events_utils = new Events__Utils()
    }

    // static properties
    static get element_name() {
        return this.name.replace    (/_/g , '-')  // Replace underscores with hyphens
                        .replace    (/--/g, '-')  // make sure we only have one hyphen
                        .toLowerCase()            // Convert to lowercase
    }

    // static methods

    static add_to_body() {
        return this.create_element_add_to_body()
    }

    static create({inner_html=null, tag=null,...attributes}={}) {
        const element = document.createElement(this.element_name);        // Create a new element using the provided tag name
        for (const [attr, value] of Object.entries(attributes)) {         // // Iterate over the attributes object and set attributes on the element
            element.setAttribute(attr, value);
        }
        if (inner_html != null) {
            element.innerHTML = inner_html;
        }
        if (tag != null) {
            element.innerHTML = tag.html();
        }
        return element;
    }

    // todo: refactor to use the create() method above (since this is adding an element to to document body which is only one of the scenarios
    static create_element() {
        return document.createElement(this.element_name);
    }

    static create_element_add_to_body() {
        const element = this.create_element();
        return document.body.appendChild(element);
    }

    static define() {
        if (!customElements.get(this.element_name)) {
            customElements.define(this.element_name, this);
            return true; }
        return false;
    }

    // instance - connection methods

    add_event_listeners__web_component() {                              // todo: see if there is a better way to do this (ie. invoke the add_event_listeners() method from this
        this.events_utils.events_receive.add_event_listener('invoke' , this.channel, this.on_invoke      );
    }

    connectedCallback() {
        this.load_attributes()
        this.channels.push(this.channel)
        this.add_event_listeners__web_component()
    }

    disconnectedCallback() {
        this.remove_event_listeners__webc_component()
    }

    load_attributes() {
        this.channel  = this.getAttribute('channel') || this.random_id('webc_channel_')
        this.webc_id  = this.getAttribute('webc_id') || this.random_id('webc_id_')
    }
    remove_event_listeners__webc_component() {
        this.events_utils.events_receive.remove_all_event_listeners()
    }

    on_invoke = (event) => {
        if (this.webc_id ===event.webc_id) {                                                    // only react to events that are sent to this specific webc_id
            let event_data = event.event_data                                                   // get the event_data
            let callback   = event.callback                                                     // get the callback
            if (typeof this[event_data.method] === 'function') {                                // check if the method defined in the method exists in this
                const result = this[event_data.method](...Object.values(event_data.params));    // if so execute it and capture the return value
                if (typeof callback === 'function') {                                           // check if the callback is a function
                    callback(result)                                                            // if it is defined, invoke it with the return value of the function execution
                }
            }
        }
    }
    // instance methods

    // events methods
    raise_event(event_name, event_detail) {
        const options =  { bubbles: false, detail: event_detail}
        this.dispatchEvent(new CustomEvent(event_name, options));
    }

    async wait_for_event(event_name, timeout) {
        const timeout_value = timeout || 100
        const timeout_message = `${event_name} event did not fire within the expected timeout value: ${timeout_value}ms.`

        await new Promise((resolve, reject) => {
            const on_timeout       = () => { reject(new Error(timeout_message)); }
            const timeout_function = setTimeout(on_timeout, timeout_value);
            const on_event         = () => { clearTimeout(timeout_function); resolve(); }
            this.addEventListener(event_name, on_event, { once: true });
        });
    }

    // other methods // todo organise these methods in a logical way
    add_adopted_stylesheet(stylesheet) {
        const currentStylesheets = this.shadowRoot.adoptedStyleSheets;
        this.shadowRoot.adoptedStyleSheets = [...currentStylesheets, stylesheet];
    }

    append_child(WebC_Class, ...attributes) {
        const child_component = WebC_Class.create(...attributes)        // calls static method create from the Web Component class
        this.appendChild(child_component)                               // adds it as a child to the current WebC
        return child_component                                          // returns the instance created of WebC_Class
    }
    // root_element() {
    //     return null
    // }

    // todo: refactor stylesheets to separate class
    add_css_rules(css_rules) {
        const styleSheet  = this.create_stylesheet_from_css_rules(css_rules) // add new style sheet to adopted stylesheets for the shadow root
        this.add_adopted_stylesheet(styleSheet)
        return styleSheet
    }

    all_css_rules() {
        const cssObject = {}
        for (let stylesheet of this.stylesheets()) {
            const cssRules = stylesheet.cssRules;
            for (let rule of cssRules) {
                cssObject[rule.selectorText] = rule.cssText; }}
        return cssObject
    }

    append_inner_html(value) {        
        this.shadowRoot.innerHTML  += value
    }

    create_stylesheet_from_css_rules(css_rules) {
        const styleSheet = new CSSStyleSheet();

        Object.entries(css_rules).forEach(([css_selector, css_properties]) => {        // Iterate over each key (selector) in cssProperties
            const css_init          = `${css_selector} {}`;                                     // note: it looks like at the moment there isn't another way to create an empty CSSStyleRule and populate it
            const rules_length      = styleSheet.cssRules.length                                // get size of css rules
            const insert_position   = styleSheet.insertRule(css_init, rules_length);            // so that we can create a new one at the end
            const cssRule           = styleSheet.cssRules[insert_position];                     // get a reference to the one we added
            this.populate_rule(cssRule, css_properties);                                        // populate new css rule with provided css properties
        });
        return styleSheet
    }

    //todo figure out what is wrong with the code below. it is almost working (to handle recursive css rules), but it adding lots of extra rules
    //     and not really working ok with nested rules (it did worked once and I think it is really close)
    // create_stylesheet_from_css_rules(css_rules) {
    //     const styleSheet = new CSSStyleSheet();
    //
    //     const process_rules = (selector, properties) => {                               // Helper function to recursively flatten the CSS rules
    //         Object.entries(properties).forEach(([key, value]) => {
    //             if (typeof value === 'object') {
    //                 process_rules(`${selector} ${key}`, value);                         // If the value is an object, it's a nested rule (e.g., '.active')
    //             } else {
    //                 if (!styleSheet.cssRules[selector]) {                               // Otherwise, it's a CSS property, so we apply it directly
    //                     const css_init = `${selector} {}`;                              // Create a new empty rule
    //                     const rules_length = styleSheet.cssRules.length;
    //                     styleSheet.insertRule(css_init, rules_length);
    //                 }
    //                 const cssRule = Array.from(styleSheet.cssRules).find(rule => rule.selectorText === selector);
    //                 cssRule.style[key] = value;
    //             }
    //         });
    //     };
    //
    //     Object.entries(css_rules).forEach(([css_selector, css_properties]) => {     // Iterate over the top-level selectors and process each rule
    //         process_rules(css_selector, css_properties);
    //     });
    //
    //     return styleSheet;
    // }


    inner_html() {
        return this.shadowRoot.innerHTML 
    }
    
    query_selector(selector) {
        return this.shadow_root().querySelector(selector)
    }

    parent_element() {
        return this.parentElement
    }

    random_id(prefix='random') {
        const random_part = Math.random().toString(36).substring(2, 7); // Generate a random string.
        return `${prefix}_${random_part}`;
    }

    set_inner_html(inner_html) {
        this.shadowRoot.innerHTML = inner_html
    }

    shadow_root() {
        return this.shadowRoot
    }

    shadow_root_append(child) {
        return this.shadowRoot.appendChild(child)
    }

    stylesheets(include_root=true, include_shadow=true) {
        const all_stylesheets =[]
        if (include_root) {
            all_stylesheets.push(...Array.from(this.shadowRoot.styleSheets)) }
        if (include_shadow) {
            all_stylesheets.push(...this.shadowRoot.adoptedStyleSheets) }
        // this is required for Safari which was duplicating the entires
        return all_stylesheets.filter((stylesheet, index, self) =>      // return unique list
            index === self.findIndex(s => s === stylesheet))
        return all_stylesheets
    }

    populate_rule(css_rule, css_properties) {
        for (let prop_name in css_properties) {
            const css_prop_name = prop_name.replace(/([A-Z])/g, '-$1').toLowerCase();           // Convert camelCase to kebab-case
            const css_prop_value = css_properties[prop_name]                                    // get css prop value
            css_rule.style.setProperty(css_prop_name, css_prop_value);                          // set property in css_rule
        }
    }

    async wait_for(duration=1000) {
        return new Promise(resolve => setTimeout(resolve, duration));
    }
}

