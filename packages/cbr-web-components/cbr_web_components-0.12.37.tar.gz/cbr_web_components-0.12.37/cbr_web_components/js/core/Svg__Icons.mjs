import Span from "./Span.mjs";

export default class Svg__Icons{
    constructor() {
    }

    picture_as_pdf(...attributes) {
        const svg_code = this.apply_attributes_to_svg_code(Svg__Icons.picture_as_pdf,...attributes)
        const span_svg = new Span({class:'icon-svg picture-as-pdf', value:svg_code})
        return span_svg
    }

    screenshot_monitor(...attributes) {
        const svg_code = this.apply_attributes_to_svg_code(Svg__Icons.screenshot_monitor,...attributes)
        return new Span({class:'icon-svg screenshot-monitor', value:svg_code})
    }

    apply_attributes_to_svg_code(svg_code, attributes) {
        const svg_element = new DOMParser().parseFromString(svg_code, 'image/svg+xml').documentElement;

        for (let [key, value] of Object.entries(attributes)) {          // Apply the attributes to the SVG element
            svg_element.setAttribute(key, value);
        }


        return new XMLSerializer().serializeToString(svg_element);       // Return the updated SVG as a string
    }

    //icons SVG from: https://fonts.google.com/icons
    static picture_as_pdf     = `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="M360-460h40v-80h40q17 0 28.5-11.5T480-580v-40q0-17-11.5-28.5T440-660h-80v200Zm40-120v-40h40v40h-40Zm120 120h80q17 0 28.5-11.5T640-500v-120q0-17-11.5-28.5T600-660h-80v200Zm40-40v-120h40v120h-40Zm120 40h40v-80h40v-40h-40v-40h40v-40h-80v200ZM320-240q-33 0-56.5-23.5T240-320v-480q0-33 23.5-56.5T320-880h480q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H320Zm0-80h480v-480H320v480ZM160-80q-33 0-56.5-23.5T80-160v-560h80v560h560v80H160Zm160-720v480-480Z"/></svg>`
    static screenshot_monitor = `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="M600-320h160v-160h-60v100H600v60ZM200-560h60v-100h100v-60H200v160Zm120 440v-80H160q-33 0-56.5-23.5T80-280v-480q0-33 23.5-56.5T160-840h640q33 0 56.5 23.5T880-760v480q0 33-23.5 56.5T800-200H640v80H320ZM160-280h640v-480H160v480Zm0 0v-480 480Z"/></svg>`
}