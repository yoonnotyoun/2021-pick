import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import Movie from '@/views/Movie'
import Basket from '@/views/Basket'
import BasketDetail from '@/views/BasketDetail'
import BasketForm from '@/views/BasketForm'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Signup from '@/views/accounts/Signup'
import SetMovieTaste from '@/views/accounts/SetMovieTaste'
import Group from '@/views/accounts/Group'

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
    path: '/basket/detail',
    name: 'BasketDetail',
    component: BasketDetail
  },
  {
    path: '/basketform',
    name: 'BasketForm',
    component: BasketForm
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
  {
    path: '/accounts/setmovietaste',
    name: 'SetMovieTaste',
    component: SetMovieTaste
  },
  {
    path: '/accounts/group',
    name: 'Group',
    component: Group
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
