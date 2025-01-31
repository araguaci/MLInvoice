<?php
/**
 * Finvoice with SOAP envelope
 *
 * PHP version 7
 *
 * Copyright (C) Ere Maijala 2010-2021
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2,
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * @category MLInvoice
 * @package  MLInvoice\Base
 * @author   Ere Maijala <ere@labs.fi>
 * @license  http://opensource.org/licenses/gpl-2.0.php GNU General Public License
 * @link     http://labs.fi/mlinvoice.eng.php
 */
require_once 'invoice_printer_xslt.php';
require_once 'htmlfuncs.php';
require_once 'miscfuncs.php';

/**
 * Finvoice with SOAP envelope
 *
 * @category MLInvoice
 * @package  MLInvoice\Base
 * @author   Ere Maijala <ere@labs.fi>
 * @license  http://opensource.org/licenses/gpl-2.0.php GNU General Public License
 * @link     http://labs.fi/mlinvoice.eng.php
 */
class InvoicePrinterFinvoiceSOAP extends InvoicePrinterXSLT
{
    /**
     * Create the printout and return headers and data
     *
     * @return array Associative array with headers and data
     */
    public function createPrintout()
    {
        // First create the actual Finvoice
        $this->xsltParams['printTransmissionDetails'] = true;
        parent::transform('create_finvoice.xsl', 'Finvoice.xsd');
        $finvoice = $this->xml;

        // Create the SOAP envelope
        parent::transform('create_finvoice_soap_envelope.xsl');

        $headers = [
            'Content-Type' => 'text/xml; charset=ISO-8859-15'
        ];
        $filename = $this->getPrintoutFileName();
        if ($this->printStyle) {
            $headers['Content-Disposition'] = "inline; filename=$filename";
        } else {
            $headers['Content-Disposition'] = "attachment; filename=$filename";
        }
        return [
            'headers' => $headers,
            'data' => $this->xml . "$finvoice"
        ];
    }
}
