$( function() {
    // smartmenus initialization
    $( "#navigation>ul").addClass("sm sm-blue");
    $( "#navigation>ul" ).smartmenus({
			subMenusSubOffsetX: 1,
			subMenusSubOffsetY: -8
    });

    // all navbar links which are not on this site (i.e., don't start with '/') open in new tab
    $( '.navbar a' ).not('[href^="/"]').attr('target', '_blank');

    // register interest group for all links
    register_group('interest', '#metanav-select-interest', 'a' );

    // get from sessionStorage if there, else localStorage
    var last_metanav_select_interest = sessionStorage.getItem('members_interest') || null;
    if (last_metanav_select_interest == null) {
        last_metanav_select_interest = localStorage.getItem('members_interest');
        // still null? this is the user's first time through -- just use the first available option
        if (last_metanav_select_interest == null) {
            last_metanav_select_interest = $( "#metanav-select-interest option:first" ).val()
        }
    }
    var metanav_select_interest = $( "#metanav-select-interest" );
    metanav_select_interest.val(last_metanav_select_interest);
    metanav_select_interest.select2({
      placeholder: 'select an interest',
      theme: "classic",
    });

    function check_redirect_url_rule() {
        // get current interest
        var metanav_new_interest = metanav_select_interest.val();
        // translate url rule using interest
        // try filtered rule first, then page rule
        var url_rule = $('#metanav-url-rule-filtered').text();
        if (url_rule == "") {
            url_rule = $('#metanav-url-rule').text();
        }
        // check for redirect only if '<interest>' in url_rule
        // TODO: but this doesn't handle multiple variables, e.g, <interest>/route/<thisid>
        var decoded_url_rule = decodeURIComponent(url_rule)
        if (decoded_url_rule.indexOf('<interest>') != -1) {
            var new_url = _.replace(decoded_url_rule, '<interest>', metanav_new_interest);
            var last_url = window.location.pathname;
            // if url_rule present, and if new url, reload page
            if ((new_url != "") && (new_url != last_url)) {
                window.location.assign(new_url);
            }
        }
    }

    metanav_select_interest.on('select2:select', function(e){
        var metanav_new_interest = metanav_select_interest.val();
        localStorage.setItem('members_interest', metanav_new_interest);
        sessionStorage.setItem('members_interest', metanav_new_interest);

        // check when interest changes, maybe redirect
        check_redirect_url_rule();
    });

    // check when page loads, maybe redirect
    check_redirect_url_rule();
});

