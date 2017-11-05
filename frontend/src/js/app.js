import Vue from 'vue'


Vue.component('test',{
    template : `<b>{{text}}</b>`,
    props: ['text']
});

var app = new Vue({
    el: '#app',
    data: {
        todos: [1,2,3,45]
    },
    template: `<div>
                <ol>
                    <li v-for="todo in todos">
                        <test v-bind:text="todo"></test>
                    </li>
                </ol>
                
                </div>`,
});

window.app = app;