<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SiteController extends Controller
{
    public function index()
    {
        $nome = "Hello Word!";

        return view('home', [
            'nome' => $nome
        ]);
    }
};
