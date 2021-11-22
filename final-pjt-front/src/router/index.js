import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import Movie from '@/views/Movie'
import MovieDetail from '@/views/MovieDetail'
import Basket from '@/views/Basket'
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
    path: '/movie/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/basket',
    name: 'Basket',
    component: Basket
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
