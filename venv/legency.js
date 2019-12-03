
output_list = Array();
/* level - 0:Summary; 1:Failed; 2:All */

function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.indexOf('testfail') === 0) {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.indexOf('testpass') === 0) {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}

function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid = 'testfail.' + cid.substr(1) + '.' + (i+1);
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'testpass.' + cid.substr(1) + '.' + (i+1);
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none';
            document.getElementById(tid).className = 'hiddenRow';
        } else {
            document.getElementById(tid).className = '';
        }
    }
}

function showTestDetail(div_id){
    var details_div = document.getElementById(div_id);
    var displayState = details_div.style.display;
    if (displayState !== 'block' ) {
        details_div.style.display = 'block';
    }
    else {
        details_div.style.display = 'none';
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
