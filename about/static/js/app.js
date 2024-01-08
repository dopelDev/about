import { createApp } from "vue";
import Header from "../vue/components/Header.vue";
import VueAlert from "../vue/components/VueAlert.vue";
import SocialMedia from "../vue/components/SocialMedia.vue";

createApp(Header).mount('#header');
createApp(VueAlert).mount('#vue-alert');
createApp(SocialMedia).mount('#social-media');

