import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import Movie from '@/views/Movie'
import Basket from '@/views/Basket'
import Tastingroom from '@/views/Tastingroom'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Signup from '@/views/accounts/Signup'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/movie',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/basket',
    name: 'Basket',
    component: Basket
  },
  {
    path: '/tastingroom',
    name: 'Tastingroom',
    component: Tastingroom
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
