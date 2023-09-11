const user_input = $("#user-input")
const category_choice = $("#category-choice")
const min_price = $("#min-price")
const max_price = $("#max-price")
const search_icon = $('#search-icon')
const listing_div = $("#replaceable-content")
const endpoint = '/homepage/listing/overview'
const delay_by_in_ms = 500
const delay_by_in_ms2 = 150
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the listing_div, then:
            listing_div.fadeTo('fast', 0).promise().then(() => {
                // replace the HTML contents
                listing_div.html(process(response['html_from_view']))
                // fade-in the div with new contents
                listing_div.fadeTo('fast', 1)
                // stop animating search icon
                search_icon.removeClass('blink')
            })
        })
}


user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val(), // value of user_input: the HTML element with ID user-input
        qs: $(category_choice).val(),
        min_price: $(min_price).val(),
        max_price: $(max_price).val()
    }

    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

category_choice.on('change', function() {
    const request_parameters = {
        q: $(user_input).val(), // value of user_input: the HTML element with ID user-input
        qs: $(this).val(),
        min_price: $(min_price).val(),
        max_price: $(max_price).val()
    }

    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms2, endpoint, request_parameters)
})

min_price.on('keyup', function () {

    const request_parameters = {
        q: $(user_input).val(), // value of user_input: the HTML element with ID user-input
        qs: $(category_choice).val(),
        min_price: $(this).val(),
        max_price: $(max_price).val()
    }

    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

max_price.on('keyup', function () {

    const request_parameters = {
        q: $(user_input).val(), // value of user_input: the HTML element with ID user-input
        qs: $(category_choice).val(),
        min_price: $(min_price).val(),
        max_price: $(this).val()
    }

    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

function process(str) {

    var div = document.createElement('div');
    div.innerHTML = str.trim();

    return format(div, 0).innerHTML;
}

function format(node, level) {

    var indentBefore = new Array(level++ + 1).join('  '),
        indentAfter  = new Array(level - 1).join('  '),
        textNode;

    for (var i = 0; i < node.children.length; i++) {

        textNode = document.createTextNode('\n' + indentBefore);
        node.insertBefore(textNode, node.children[i]);

        format(node.children[i], level);

        if (node.lastElementChild == node.children[i]) {
            textNode = document.createTextNode('\n' + indentAfter);
            node.appendChild(textNode);
        }
    }

    return node;
}

          