<%inherit file="${context['main_template'].uri}" />
<%namespace file="/base/pager.mako" import="pager"/>
<%namespace file="/base/pager.mako" import="sortable"/>
<%namespace file="/base/searchformlayout.mako" import="searchform"/>

<%block name='content'>

${searchform()}

<div>
    <div>
        ${records.item_count} Résultat(s)
    </div>
    <div class="align_right">
        <small>Les montants sont exprimés TTC</small>
    </div>
    <div class='table_container'>
        ${request.layout_manager.render_panel('business_list', records, is_admin_view=is_admin)}
    </div>
    ${pager(records)}
</div>

</%block>
