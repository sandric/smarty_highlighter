<?php

    /*
    smarty plugin to be evaluated from your code
    */
    function smarty_function_smarty_highlighter($params, &$smarty)
    {

        if(!smarty_highlighter)
            return false;

        $host = isset($params['host']) ? $params['host'] : "localhost";
        $port = isset($params['port']) ? $params['port'] :  8888;
        $uri = isset($params['uri']) ? $params['uri'] :  "/ws";

	//here you run your function for template drawing
        return tpl::get(
                        'smarty_highlighter.htm',
                        array(
                           'host' => $host,
                           'port' => $port,
                           'uri' => $uri,
                        )
        );
    }
?>
