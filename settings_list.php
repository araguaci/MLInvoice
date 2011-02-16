<?php
/*******************************************************************************
VLLasku: web-based invoicing application.
Copyright (C) 2010-2011 Ere Maijala

This program is free software. See attached LICENSE.

*******************************************************************************/

/*******************************************************************************
VLLasku: web-pohjainen laskutusohjelma.
Copyright (C) 2010-2011 Ere Maijala

T�m� ohjelma on vapaa. Lue oheinen LICENSE.

*******************************************************************************/

require_once "sqlfuncs.php";
require_once "miscfuncs.php";
require_once "localize.php";

function createSettingsList()
{
  if ($_SESSION['sesACCESSLEVEL'] != 99 )
  {
?>
  <div class="form_container">
    <?php echo $GLOBALS['locNOACCESS'] . "\n"?>
  </div>
<?php
    return;
  }
  
  require 'settings_def.php';

  $messages = '';

  $blnSave = getPostRequest('saveact', FALSE) ? TRUE : FALSE;
  if ($blnSave)
  {
    foreach ($arrSettings as $name => $elem)
    {
      if ($elem['type'] == 'LABEL')
        continue;
      $newValue = getPost($name, NULL);
      if (!isset($newValue))
      {
        if (!$elem['allow_null'])
        {
          $messages .= $GLOBALS['locERRVALUEMISSING'] . ": $name<br>\n";
          continue;
        }
        else
        {
          $newValue = '';
        }
      }
      if ($elem['type'] == 'CURRENCY' || $elem['type'] == 'PERCENT')
        $newValue = str_replace(",", ".", $newValue);
        
      if (isset($elem['session']) && $elem['session'])
        $_SESSION[$name] = $newValue;
      mysql_param_query('DELETE from {prefix}settings WHERE name=?', array($name));
      mysql_param_query('INSERT INTO {prefix}settings (name, value) VALUES (?, ?)', array($name, $newValue));
    }
  }
?>
  <div class="form_container">
    <div class="message"><?php echo $messages?></div>
  
    <script type="text/javascript">
    <!--
    $(document).ready(function() {
      $('input[class~="hasCalendar"]').datepicker();
      $('iframe[class~="resizable"]').load(function() {
        var iframe = $(this);
        var body = iframe.contents().find("body");
        var newHeight = body.outerHeight(true) + 10;
        // Leave room for calendar popup
        if (newHeight < 250)
          newHeight = 250;
        iframe.css("height", newHeight + 'px');
        body.css("overflow", "hidden");
      });   
      $('#admin_form').find('input[type="text"],input[type="checkbox"],select,textarea').change(function() { $('.save_button').addClass('unsaved'); });
    });
    -->
    </script>
  
    <?php createSettingsListButtons()?>
    <div class="form">
    <form method="post" action="" name="admin_form" id="admin_form">
<?php
    foreach ($arrSettings as $name => $elem)
    {
      $elemType = $elem['type'];
      if ($elemType == 'LABEL')
      {
?>
        <div class="sublabel" style="clear: both; margin-top: 10px"><?php echo $elem['label']?></div>
<?php        
        continue;
      }
      $value = getPost($name, NULL);
      if (!isset($value))
      {
        if (isset($elem['session']) && $elem['session'])
        {
          $value = isset($_SESSION[$name]) ? $_SESSION[$name] : (isset($elem['default']) ? cond_utf8_encode($elem['default']) : '');
        }
        else
        {
          $res = mysql_param_query('SELECT value from {prefix}settings WHERE name=?', array($name));
          if ($row = mysql_fetch_assoc($res))
            $value = $row['value'];
          else
            $value = isset($elem['default']) ? cond_utf8_encode($elem['default']) : '';
        }
          
        if ($elemType == 'CURRENCY')
          $value = miscRound2Decim($value);
        elseif ($elemType == 'PERCENT')
          $value = miscRound2Decim($value, 1);
      }
      if ($elemType == 'CURRENCY' || $elemType == 'PERCENT')
        $elemType = 'INT';
?>
      <div class="label" style="clear: both"><label for="<?php echo $name?>"><?php echo $elem['label']?></label></div>
      <div class="field" style="clear: both">
        <?php echo htmlFormElement($name, $elemType, $value, $elem['style'], '', "MODIFY", '', '', array(), isset($elem['elem_attributes']) ? $elem['elem_attributes'] : '')?>
      </div>
<?php        
    }
?>      
    <input type="hidden" name="saveact" value="0">
    <?php createSettingsListButtons()?>
    </form>
    </div>
  </div>
<?php
}

function createSettingsListButtons()
{
?>
<div class="form_buttons" style="clear: both">
      <a class="actionlink save_button" href="#" onclick="document.getElementById('admin_form').saveact.value=1; document.getElementById('admin_form').submit(); return false;"><?php echo $GLOBALS['locSAVE']?></a>
    </div>
<?php
}
